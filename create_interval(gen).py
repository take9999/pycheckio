import itertools


def create_intervals(data):
    t = 0
    for r, g in itertools.groupby(x - i for i, x in enumerate(sorted(data))):
        s = t
        for x in g: s += 1
        yield r + t, r + s - 1
        t = s

