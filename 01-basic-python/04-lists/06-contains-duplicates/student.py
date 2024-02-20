def contains_duplicates(xs):
    xs = sorted(xs)
    for i in range(0 , len(xs)-1):
        if xs[i] == xs[i+1]:
            return True
    return False