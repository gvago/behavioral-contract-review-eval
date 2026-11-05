class Store:
    def __init__(self, rows):
        self.rows = rows

    def archive(self, resource_id):
        self.rows[resource_id]['state'] = 'archived'

    def delete(self, resource_id):
        del self.rows[resource_id]

    def delete_named(self, name, environment):
        for key, row in list(self.rows.items()):
            if row['name'] == name and row['environment'] == environment:
                del self.rows[key]

    def current(self, resource_id):
        return self.rows[resource_id]
