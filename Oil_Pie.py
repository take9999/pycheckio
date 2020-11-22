from fractions import Fraction


def divide_pie(groups):
    num_members = sum([abs(x) for x in groups])
    remain = Fraction(1, 1)

    for one_group in groups:
        if one_group >= 0:
            remain -= Fraction(one_group, num_members)
        else:
            remain *= 1 - Fraction(abs(one_group), num_members)

    if remain <= 0:
        remain = 0

    return remain.numerator, remain.denominator


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    # (6, 6) -> (4, 6)=(12, 18) -> (10, 18) -> (1, 18)
    # 分子をnum_membersで割り切れる値にしてから計算（知っている場合は初回のみ、知らない場合は次回以降も）
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
    assert tuple(divide_pie([99, -99])) == (1, 4), ""
