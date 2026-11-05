def may_compact(archived, legal_hold):
    return archived and not legal_hold
