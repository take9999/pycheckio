from typing import List, Tuple
import math


# 2つの円が交わっているかどうか判定
def is_intersect(circle_a: Tuple, circle_b: Tuple) -> bool:
    x_a, y_a, rad_a = circle_a[0], circle_a[1], circle_a[2]
    x_b, y_b, rad_b = circle_b[0], circle_b[1], circle_b[2]
    distance_center = math.sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2)

    d_sub = abs(rad_a - rad_b)
    d_sum = rad_a + rad_b

    # 外接している　もしくは　2つの円が離れている
    if d_sum <= distance_center:
        return False
    # 内接している　もしくは　片方の円がもう片方の中に入っている
    elif distance_center <= d_sub:
        return False
    # 交わっている
    else:
        return True


# 交わった円グループの数を返す
def count_chains(circles_list: List) -> int:
    len_circles = len(circles_list)
    chains_num = 0
    seen = [False] * len_circles

    def dfs(circle_idx):
        stack = [circle_idx]
        seen[circle_idx] = True

        while stack:
            idx = stack.pop()
            for i, one_circle in enumerate(circles_list):
                if idx == i or seen[i] or not is_intersect(circles_list[idx], one_circle):
                    continue
                seen[i] = True
                stack.append(i)

    for x in range(len_circles):
        if seen[x]:
            continue
        chains_num += 1
        dfs(x)

    return chains_num


if __name__ == '__main__':
    print("Example:")
    # print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    # assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    # assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    # assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    # assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    # assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    assert count_chains([[0, 0, 2], [1, 0, 3], [3, 0, 1], [2, 1, 1], [-2, -2, 1], [0, 0, 4], [-3, 0, 1]]) == 3, ""
    print("Coding complete? Click 'Check' to earn cool rewards!")
