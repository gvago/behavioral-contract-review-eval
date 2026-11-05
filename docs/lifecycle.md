# Resource lifecycle
Archiving changes the resource state to archived. The payload is retained for later restoration.
Resource names are unique inside an environment, not across environments. Cleanup affects only the requested environment.
Planning and application are separate requests. A resource may be protected after planning. Protected resources cannot be deleted, including through an old plan.
