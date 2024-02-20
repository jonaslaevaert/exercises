def target_sum(ns, target):
    for x in range(0, len(ns)):
        for y in range(0, len(ns)):
            if ns[x]+ns[y] == target and x != y:
                return True
    return False
