class Snapshots:
    def __init__(self):
        self.owners = {'shared': {'alice', 'bob'}}
        self.deleted = []

    def detach(self, snapshot, owner):
        self.owners[snapshot].remove(owner)

    def destroy(self, snapshot):
        self.deleted.append(snapshot)


def parse_enabled(value):
    if value in ('yes', 'true', '1'):
        return True
    if value in ('no', 'false', '0'):
        return False
    raise ValueError(value)


def backup(schedule, weekdays):
    return schedule and weekdays
