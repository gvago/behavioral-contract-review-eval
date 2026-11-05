# Retry behavior
When retries are enabled, only HTTP 503 responses are retried. HTTP 429 is returned to the caller.
