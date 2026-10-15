import pytest
from rest_framework.test import APIClient
from apps.catalog.models import GameCategory
from apps.common.cache import (
    get_cache_version,
    invalidate_catalog_cache,
    safe_cache_get,
    safe_cache_set
)


@pytest.mark.django_db
class TestHealthProbesAndCache:
    def setup_method(self):
        self.client = APIClient()

    def test_liveness_probe_returns_200(self):
        # Liveness must return 200 directly without touching DB
        response = self.client.get('/api/v1/health/live/')
        assert response.status_code == 200
        assert response.data['status'] == 'alive'

    def test_readiness_probe_returns_200_when_db_ok(self):
        response = self.client.get('/api/v1/health/ready/')
        assert response.status_code == 200
        assert response.data['status'] == 'ready'
        assert response.data['database'] == 'connected'

    def test_cache_safe_fallback_operations(self):
        # Test safe get and safe set
        safe_cache_set('test_key', {'foo': 'bar'}, timeout=10)
        cached = safe_cache_get('test_key')
        assert cached == {'foo': 'bar'}

        # Test cache versioning & invalidation
        v1 = get_cache_version('catalog')
        invalidate_catalog_cache()
        v2 = get_cache_version('catalog')
        assert v2 > v1

    def test_catalog_category_caching(self):
        GameCategory.objects.create(slug='test-cat', title='Test Kategoriya')

        # First request populates cache
        resp1 = self.client.get('/api/v1/categories/')
        assert resp1.status_code == 200

        # Second request reads from cache
        resp2 = self.client.get('/api/v1/categories/')
        assert resp2.status_code == 200
        assert resp2.data == resp1.data
