import itertools


def create_intervals(data):
    t = 0
    iter_goupby = itertools.groupby(x - i for i, x in enumerate(sorted(data)))
    for r, g in iter_goupby:
        s = t
        for x in g:
            s += 1
        yield r + t, r + s - 1
        t = s


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # add a check whether it is really a generator
    import types

    assert isinstance(create_intervals([]), types.GeneratorType), "it should be a generator"
    # add list(...) to match to right value
    print(list(create_intervals([8, 7])))
    print(list(create_intervals([1, 3, 7])))

    assert list(create_intervals({1, 2, 3, 4, 5, 7, 8, 12})) == [(1, 5), (7, 8), (12, 12)], "First"
    assert list(create_intervals({1, 2, 3, 6, 7, 8, 4, 5})) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
