# def rotate(xs, n):
#     ns = xs[:n]
#     ys = xs[n:]
#     return [*ys, *ns]

def rotate(xs, n):
    for _ in range(n):
        x = xs.pop(0)
        xs.append(x)
