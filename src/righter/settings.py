import os

REQUESTS_CACHE_BACKEND = os.environ.get("REQUESTS_CACHE_BACKEND", "sqlite")
