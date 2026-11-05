from workspace.common import normalize_account


def find_account(accounts, raw_name):
    return accounts.get(normalize_account(raw_name))
