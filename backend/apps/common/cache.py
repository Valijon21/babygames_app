import logging
from django.core.cache import cache

logger = logging.getLogger('bolajon.cache')

CATALOG_CACHE_VERSION_KEY = 'bolajon:cache_version:catalog'
DEFAULT_TTL = 300  # 5 minutes


def get_cache_version(namespace: str = 'catalog') -> int:
    """
    Get current version number for cache namespace.
    Incrementing this instantly invalidates all keys in this namespace without flushall.
    """
    key = f'bolajon:cache_version:{namespace}'
    try:
        version = cache.get(key)
        if version is None:
            version = 1
            cache.set(key, version, timeout=None)
        return int(version)
    except Exception as exc:
        logger.warning("Cache service unavailable when fetching version (%s). Falling back.", exc)
        return 1


def invalidate_catalog_cache():
    """
    BJ-128: Invalidate entire catalog cache namespace by bumping version.
    Zero-downtime, O(1) time complexity, safe against Redis unavailability.
    """
    key = CATALOG_CACHE_VERSION_KEY
    try:
        try:
            cache.incr(key)
        except Exception:
            # Key might not exist yet or cache provider does not support incr
            cur = get_cache_version('catalog')
            cache.set(key, cur + 1, timeout=None)
        logger.info("Catalog cache namespace successfully invalidated.")
    except Exception as exc:
        logger.warning("Cache invalidation failed (Redis possibly down): %s", exc)


def safe_cache_get(key: str, default=None):
    """
    BJ-128: Retrieve a value from cache with graceful degradation if Redis is down.
    """
    try:
        return cache.get(key, default)
    except Exception as exc:
        logger.warning("Cache GET failed for key '%s': %s. Falling back to DB.", key, exc)
        return default


def safe_cache_set(key: str, value, timeout: int = DEFAULT_TTL):
    """
    BJ-128: Store a value in cache safely with graceful degradation if Redis is down.
    """
    try:
        cache.set(key, value, timeout=timeout)
    except Exception as exc:
        logger.warning("Cache SET failed for key '%s': %s.", key, exc)
