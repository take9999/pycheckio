def capture(matrix):
    free = list(range(1, len(matrix)))

    infected = [0]
    t = 0

    # freeが無くなったら、全て侵食されたとして終了
    while free:
        t += 1
        underattack = []

        for i in infected:
            for j in free:
                if matrix[i][j] == 1 and j not in underattack:
                    underattack.append(j)

        # underattackは侵食中のindexリスト
        # matrix[j][j]の耐久時間を減らしていき、0になったら侵食されたとする。
        for j in underattack:
            matrix[j][j] -= 1
            if matrix[j][j] == 0:
                free.remove(j)
                infected.append(j)

    return t


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
