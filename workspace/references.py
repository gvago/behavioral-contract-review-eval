def remove_owner(snapshots, snapshot, owner):
    snapshots.detach(snapshot, owner)
    if not snapshots.owners[snapshot]:
        snapshots.destroy(snapshot)
