def merge_intervals(intervals):
    result = []
    interv = []

    for itr in intervals:
        interv.append([itr[0], itr[1]])
    interv.sort()
    res = []

    while (len(interv) > 0):
        if len(interv) == 1:
            res.append(interv[0])
            interv.pop(0)
            continue
        if interv[0][1]+1 >= interv[1][0]:
            tmp = [interv[0][0], max(interv[0][1], interv[1][1])]
            interv[0] = tmp
            interv.pop(1)
            continue
        res.append(interv[0])
        interv.pop(0)

    for r in res:
        result.append((r[0], r[1]))

    print(result)
    return iter(result)


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    res = merge_intervals(iter([(1, 12), (2, 3), (4, 7)]))
    assert hasattr(res, '__iter__'), "your function should return the iterator object"
    assert hasattr(res, '__next__'), "your function should return the iterator object"

    assert list(merge_intervals(iter([(1, 4), (2, 6), (8, 10), (12, 19)]))) == [
        (1, 6), (8, 10), (12, 19)], "First"
    assert list(merge_intervals(iter([(1, 12), (2, 3), (4, 7)]))) == [
        (1, 12)], "Second"
    assert list(merge_intervals(iter([(1, 5), (6, 10), (10, 15), (17, 20)]))) == [
        (1, 15), (17, 20)], "Third"
    print('Done! Go ahead and Check IT')
