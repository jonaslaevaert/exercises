def includes(xs, ys):
    for i in range (0 , len(ys)):
        if ys[i] not in xs:
            return False
    return True
