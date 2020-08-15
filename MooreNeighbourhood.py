import pprint


# 与えられたエリア全体の周囲に0パディングを行う
def add_padding(grid):
    max_col, max_row = len(grid[0]), len(grid)

    # 先頭に要素が全て0のlistを追加
    pad_grid = [[0 for x in range(max_col+2)]]

    # 右端、左端に要素0を追加
    for r in range(max_row):
        r_list_grid = list(grid[r])
        r_list_grid.append(0)
        r_list_grid.insert(0, 0)
        pad_grid.append(r_list_grid)

    # 末尾に要素が全て0のlistを追加
    pad_grid.append([0 for x in range(max_col+2)])

    return pad_grid


# ターゲットの座標の周囲にある"1"を集計
def count_neighbours_pad(grid, target_row, target_col):
    count = 0

    for row in range(-1, 2):
        for col in range(-1, 2):
            if row == 0 and col == 0:
                pass
            else:
                count += grid[target_row + row][target_col + col]
    # print(count)
    
    return count


def count_neighbours(grid, row, col):
    pad_grid = add_padding(grid)
    # print.pprint(pad_grid)

    row_after_pad = row + 1
    col_after_pad = col + 1

    answer = count_neighbours_pad(pad_grid, row_after_pad, col_after_pad)
    return answer


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"



