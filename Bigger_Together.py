import itertools
import math


def get_big_num(ints):
    str_ints = [str(x) for x in ints]
    p = itertools.permutations(str_ints, len(str_ints))
    max = -math.inf
    for v in p:
        num = int("".join(v))
        if num > max:
            max = num
    return max


def get_min_num(ints):
    str_ints = [str(x) for x in ints]
    p = itertools.permutations(str_ints, len(str_ints))
    min = math.inf
    for v in p:
        num = int("".join(v))
        if num < min:
            min = num
    return min


# def bigger_together(ints):
#     return get_big_num(ints) - get_min_num(ints)


def bigger_together(ints):
    def f(ints, key):
        res = ''
        s = [str(i) for i in ints]

        while (s):
            t = s[0]
            for k in s[1:]:
                t = k if key(k + t, t + k) == k + t else t
            res += t
            s.remove(t)

        return int(res)

    return f(ints, key=max) - f(ints, key=min)



if __name__ == '__main__':
    bigger_together([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    assert bigger_together([1, 2, 3, 4]) == 3087, "4321 - 1234"
    assert bigger_together([1, 2, 3, 4, 11, 12]) == 32099877, "43212111 - 11112234"
    assert bigger_together([0, 1]) == 9, "10 - 01"
    assert bigger_together([100]) == 0, "100 - 100"
    print('Done! I feel like you good enough to click Check')
