def min(*args, **kwargs):
    print("args", args, "kwargs", kwargs)
    key = kwargs.get("key", None)
    value = None
    target_iter = None
    if len(args) == 1:
        target_iter = args[0]
    else:
        target_iter = args

    if key is not None:
        tmp_list = list(map(key, target_iter))
        min_val = None
        min_idx = None
        # get min index
        for i, t in enumerate(tmp_list):
            if min_val == None:
                min_val = t
                min_idx = i
            elif t < min_val:
                min_val = t
                min_idx = i
        value = target_iter[min_idx]
    else:
        value = sorted(target_iter)[0]

    return value


def max(*args, **kwargs):
    print("args", args, "kwargs", kwargs)
    key = kwargs.get("key", None)
    value = None
    target_iter = None
    if len(args) == 1:
        target_iter = args[0]
    else:
        target_iter = args

    if key is not None:
        tmp_list = list(map(key, target_iter))
        max_val = None
        max_idx = None
        # get min index
        for i, t in enumerate(tmp_list):
            if max_val == None:
                max_val = t
                max_idx = i
            elif t > max_val:
                max_val = t
                max_idx = i
        value = target_iter[max_idx]
    else:
        value = sorted(target_iter, reverse=True)[0]

    return value

#
# def min(*args, **kwargs):
#     key = kwargs.get("key", None)
#     if len(args) == 1:
#         return sorted(*args, key=key)[0]
#     else:
#         return sorted(args, key=key)[0]
#
#
# def max(*args, **kwargs):
#     key = kwargs.get("key", None)
#     if len(args) == 1:
#         return sorted(*args, key=key, reverse=True)[0]
#     else:
#         return sorted(args, key=key, reverse=True)[0]


if __name__ == '__main__':
    max(2.2, 5.6, 5.9, key=int)

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")