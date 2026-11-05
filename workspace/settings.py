from workspace.snapshots import parse_enabled


def read_enabled(values, key):
    return parse_enabled(values[key])
