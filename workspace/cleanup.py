def cleanup(store, name, environment):
    for key, row in list(store.rows.items()):
        if row['name'] == name:
            del store.rows[key]
