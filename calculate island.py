import itertools

# {(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, 0), (1, -1), (1, 1)}
# ADJACENT = {p for p in itertools.product([-1, 0, 1], repeat=2)} - {(0, 0)}
DIRECTIONS = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, 0), (1, -1), (1, 1)]

def checkio(data):
    def get_island_size(start):
        size = 0
        stack = [start]
        while stack:
            x, y = stack.pop()
            if 0 <= x < w and 0 <= y < h and unchecked[y][x]:
                unchecked[y][x] = False
                size += 1
                # 周囲8方向に島があるか探索
                stack += [(x + p[0], y + p[1]) for p in DIRECTIONS]
        return size

    h, w = len(data), len(data[0])
    unchecked = [[data[y][x] == 1 for x in range(w)] for y in range(h)]
    pts = [(x, y) for y in range(h) for x in range(w)]
    result = [get_island_size(pt) for pt in pts]

    return sorted(r for r in result if r > 0)


if __name__ == '__main__':
    print("Example:")
    print(checkio([[0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0]]))

    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
