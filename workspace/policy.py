DEFAULT_TTL = 300


def should_retry(status, enabled):
    return enabled and status == 503


def publish(target, prepare, send):
    prepare(target)
    send(target)


def load_config(path):
    try:
        return path.read_text()
    except FileNotFoundError:
        return '{}'
