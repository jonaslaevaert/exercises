def contains_duplicates(xs):
    ns = set(xs)
    return len(ns) < len(xs)
