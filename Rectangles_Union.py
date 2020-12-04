from typing import List, Tuple


def rectangles_union(recs: List[Tuple[int]]) -> int:
    rectangles_area = set()
    for r in recs:
        c_left, c_right = r[0], r[2]
        c_top, c_bottom = r[1], r[3]
        for x in range(c_left, c_right):
            for y in range(c_top, c_bottom):
                c_str = str(x) + "_" + str(y)
                rectangles_area.add(c_str)
    return len(rectangles_area)


if __name__ == '__main__':
    print("Example:")
    print(rectangles_union([
        (6, 3, 8, 10),
        (4, 8, 11, 10),
        (16, 8, 19, 11)
    ]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert rectangles_union([
        (6, 3, 8, 10),
        (4, 8, 11, 10),
        (16, 8, 19, 11)
    ]) == 33
    assert rectangles_union([
        (16, 8, 19, 11)
    ]) == 9
    assert rectangles_union([
        (16, 8, 19, 11),
        (16, 8, 19, 11)
    ]) == 9
    assert rectangles_union([
        (16, 8, 16, 8)
    ]) == 0
    assert rectangles_union([

    ]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
