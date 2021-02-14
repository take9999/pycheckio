def navigation(seaside):
    total_move_count = 0
    Y_row = 0
    Y_col = 0
    MAX_ROW = len(seaside) - 1
    MAX_COL = len(seaside[0]) - 1
    find_flag = {"M": False, "S": False, "C": False}

    # Yの位置を探索
    for i, row in enumerate(seaside):
        for j, r in enumerate(row):
            if r == "Y":
                Y_row = i
                Y_col = j

    # Yの周囲を1マスずつ拡大しながら、M,C,Sを探索
    MAX_ACTION = MAX_COL if MAX_COL > MAX_ROW else MAX_ROW
    for k in range(1, MAX_ACTION + 1):

        # 0または最大値を超えないようにする
        min_row = Y_row - k if (Y_row - k) > 0 else 0
        min_col = Y_col - k if (Y_col - k) > 0 else 0
        max_row = Y_row + k if (Y_row + k) < MAX_ROW else MAX_ROW
        max_col = Y_col + k if (Y_col + k) < MAX_COL else MAX_COL

        # 捜査範囲内でM,C,Sを探索
        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                cell_value = seaside[row][col]
                # 発見したら現在の行動回数をtotal_move_countに加算
                if cell_value in ["M", "S", "C"] and find_flag[cell_value] is False:
                    total_move_count += k
                    find_flag[cell_value] = True

    return total_move_count


if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      ['M', 0, 0, 0, 'S']]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[0, 0, 'C'],
                       [0, 'S', 0],
                       ['M', 'Y', 0]]) == 4

    assert navigation([[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 'M', 0, 'S', 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 'C', 0, 0, 0],
                       [0, 'Y', 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")
