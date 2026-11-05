import time
from workspace.common import cache_put


def save_session(cache, key, value, ttl_seconds):
    cache_put(cache, key, value, expires_at=time.time() + ttl_seconds)
