import time


def normalize_account(value):
    return value.strip().casefold()


def cache_put(cache, key, value, *, expires_at):
    cache[key] = (value, expires_at)


def cache_get(cache, key, now):
    value, expires_at = cache[key]
    return value if expires_at > now else None


def notify(sender):
    sender.send('done')


def credit(balance, amount):
    return balance + amount
