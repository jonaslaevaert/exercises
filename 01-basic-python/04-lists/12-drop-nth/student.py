def drop_nth(xs, n):
    ns = xs[:n]
    ys = xs[n+1:]
    return [*ns, *ys]
