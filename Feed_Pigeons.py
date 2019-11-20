def checkio(number):
    '''
    :param number: 餌の数
    :return: 餌がもらえた鳩の最大数
    '''

    pidgeons = 0
    next_add_num = 1
    while True:
        # 鳩より餌の数が少なくなったら、鳩の数を最大として返却
        if number <= pidgeons:
            return pidgeons

        else:
            # 鳩より餌の数が多い場合、次の鳩が飛んでくるのを待つ
            pidgeons += next_add_num
            if number < pidgeons:
                return number

            # 鳩の数だけ餌を減らす
            number -= pidgeons

            # 次に飛んでくる鳩の数を更新
            next_add_num += 1

# https://www.spicysoft.com/blog/spicy_tech/001360.html
# def checkio(number):
#     W = (number * 6) ** (1 / 3)
#     s = math.floor(W) + 1
#     e = min(math.ceil(W) - 3 + 1, 1)
#     n = s
#     maxFeededPigeons = 0
#
#     while e <= n:
#         # math.floor:小数点切り捨て
#         maxFeededPigeons = math.floor(number - n * (n - 1) * (n + 1) / 6)
#         if 0 < maxFeededPigeons:
#             maxFeededPigeons = max(maxFeededPigeons, math.floor(n * (n - 1) / 2))
#             break
#         n = n - 1
#
#     return maxFeededPigeons


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
