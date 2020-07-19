
def change2xy(target):
    alp, num = target[0], int(target[1]) - 1
    alp_num = ord(alp) - 65
    return alp_num, num


# https://www.redblobgames.com/grids/hexagons/
def find_enemy(you, dir, enemy):
    your_col, your_row = change2xy(you)
    your_x = your_col
    your_z = your_row - (your_col - (your_col & 1)) / 2
    your_y = -your_x - your_z

    enemy_col, enemy_row = change2xy(enemy)
    enemy_x = enemy_col
    enemy_z = enemy_row - (enemy_col - (enemy_col & 1)) / 2
    enemy_y = -enemy_x - enemy_z
    
    distance = int((abs(your_x - enemy_x) + abs(your_y - enemy_y) + abs(your_z - enemy_z)) / 2)
    print("x,y,z", your_x-enemy_x, your_y-enemy_y, your_z-enemy_z)


    pass


if __name__ == '__main__':
    assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
    print("You are good to go!")

