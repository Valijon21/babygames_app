import os
import sys
import time
import statistics
import django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.conf import settings  # noqa: E402
settings.REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
    'anon': '10000/minute',
    'user': '10000/minute',
}

from rest_framework.test import APIClient  # noqa: E402
from apps.accounts.models import User  # noqa: E402
from apps.child_profiles.models import ChildProfile  # noqa: E402
from apps.catalog.models import GameCategory, Game  # noqa: E402


def run_benchmark(iterations=100):
    client = APIClient()

    # Pre-seed test data
    guardian, _ = User.objects.get_or_create(
        username='load_guardian', email='load@bolajon.uz', defaults={'password': 'Pass123!Password'}
    )
    child, _ = ChildProfile.objects.get_or_create(
        guardian=guardian, display_name='LoadBot', age_band='4-5'
    )
    category, _ = GameCategory.objects.get_or_create(
        slug='load-cat', defaults={'title': 'Load Test Category'}
    )
    game, _ = Game.objects.get_or_create(
        slug='load-game',
        defaults={'category': category, 'title': 'Load Game', 'status': 'published'}
    )

    endpoints = [
        ('GET', '/api/v1/health/live/', None, False),
        ('GET', '/api/v1/health/ready/', None, False),
        ('GET', '/api/v1/categories/', None, False),
        ('GET', '/api/v1/games/', None, False),
        ('GET', f'/api/v1/games/{game.slug}/', None, False),
        ('GET', f'/api/v1/progress/children/{child.id}/summary/', None, True),
    ]

    latencies = []
    errors = 0
    total_requests = 0

    print(f"==> Launching load test simulation ({iterations} iterations per endpoint)...")
    start_time = time.time()

    for _ in range(iterations):
        for method, url, payload, auth in endpoints:
            total_requests += 1
            if auth:
                client.force_authenticate(user=guardian)
            else:
                client.force_authenticate(user=None)

            t0 = time.perf_counter()
            if method == 'GET':
                resp = client.get(url)
            elif method == 'POST':
                resp = client.post(url, payload, format='json')
            t1 = time.perf_counter()

            duration_ms = (t1 - t0) * 1000
            latencies.append(duration_ms)

            if resp.status_code >= 400:
                errors += 1

    total_duration = time.time() - start_time
    rps = total_requests / total_duration if total_duration > 0 else 0

    p50 = statistics.median(latencies)
    p90 = statistics.quantiles(latencies, n=10)[8] if len(latencies) >= 10 else p50
    p99 = statistics.quantiles(latencies, n=100)[98] if len(latencies) >= 100 else p90

    print("\n" + "=" * 50)
    print("      BOLAJON LOAD TEST BENCHMARK RESULTS")
    print("=" * 50)
    print(f"Total Requests:      {total_requests}")
    print(f"Elapsed Time:        {total_duration:.2f} s")
    print(f"Throughput (RPS):    {rps:.1f} req/s")
    print(f"Error Rate:          {errors / total_requests * 100:.2f}% ({errors} errors)")
    print(f"Latency p50:         {p50:.2f} ms")
    print(f"Latency p90:         {p90:.2f} ms")
    print(f"Latency p99:         {p99:.2f} ms")
    print(f"Latency Max:         {max(latencies):.2f} ms")
    print("=" * 50)

    assert errors == 0, f"Load test encountered {errors} errors!"
    assert p90 < 50, f"p90 latency too high: {p90:.2f}ms"
    print("==> Load test PASSED all SLA targets!\n")


if __name__ == '__main__':
    run_benchmark(50)
