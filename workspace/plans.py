def plan(store, resource_id):
    if store.current(resource_id)['protected']:
        raise ValueError('protected')
    return resource_id


def apply(store, resource_id):
    store.delete(resource_id)
