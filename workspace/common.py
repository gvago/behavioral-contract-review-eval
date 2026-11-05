import time


def normalize_account(value):
    return value.strip().casefold()


def cache_put(cache, key, value, *, expires_at):
    cache[key] = (value, expires_at)


def credit(balance, amount):
    return balance + amount
