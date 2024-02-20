def median(ns):
    ns = sorted(ns)
    if len(ns) % 2 == 1:
        return ns[len(ns)//2]
    else:
        mediaan = (ns[len(ns)//2] + ns[len(ns)//2-1])/2
        return mediaan
