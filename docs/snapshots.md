# Snapshot retention
Detaching one owner removes only that owner's reference. A snapshot with remaining owners must not be destroyed.
Enabled settings use parse_enabled; the string 'false' is false, not truthy.
Backups run only when a schedule exists and today is a weekday.
