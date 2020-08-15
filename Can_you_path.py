# return friends_list whitch match start value
def make_friends_list(matrix, target_value):
    row = len(matrix)
    col = len(matrix[0])
    # print(row, col)

    f_list = []

    for r in range(row):
        for c in range(col):
            tmp_list = []

            # up
            if r - 1 < 0:
                pass
            else:
                if matrix[r][c] == matrix[r - 1][c] == target_value:
                    tmp_list.append((r - 1, c))

            # down
            if r + 1 >= row:
                pass
            else:
                if matrix[r][c] == matrix[r + 1][c] == target_value:
                    tmp_list.append((r + 1, c))

            # left
            if c - 1 < 0:
                pass
            else:
                if matrix[r][c] == matrix[r][c - 1] == target_value:
                    tmp_list.append((r, c - 1))

            # right
            if c + 1 >= col:
                pass
            else:
                if matrix[r][c] == matrix[r][c + 1] == target_value:
                    tmp_list.append((r, c + 1))

            # print(r, c, tmp_list)
            f_list.append(tmp_list)
    print(f_list)

    return f_list


def can_pass(matrix, first, second):
    network = make_friends_list(matrix, matrix[first[0]][first[1]])

    setlist = []
    for connection in network:
        s = ab = set(connection)

        # unify all set related to a, b
        for t in setlist[:]:  # we need to use copy
            if t & ab:  # check t include a, b
                s |= t
                setlist.remove(t)
        setlist.append(s)  # only s include a, b
    return any(set([first, second]) <= s for s in setlist)


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) is True, 'First example'

    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) is False, 'First example'
