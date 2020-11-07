import math


def checkio(radius):
    # 原点に対して右上のエリアにおいて、完全な正方形のタイルと部分的なタイルの枚数をカウントして4倍する
    # radius * radius の四角形内の全ての四角形をひとつずつ見ていく
    # ひとつの四角形に着目した場合、その四角形の状態は以下の通り判定できる
    # 　distance_left_bottom：四角形の左下点の原点からの距離
    #   distance_right_top：四角形の右上点の原点からの距離
    # 　円の外にある場合：radius <= distance_left_bottom
    # 　部分的な正方形タイルの場合：distance_left_bottom < radius and distance_right_top < radius
    # 　完全な正方形タイルの場合：distance_right_top <= radius
    cnt = [0, 0]

    for y in range(math.ceil(radius)):
        for x in range(math.ceil(radius)):
            distance_left_bottom = math.sqrt(x**2 + y**2)
            distance_right_top = math.sqrt((x+1)**2 + (y+1)**2)
            if radius <= distance_left_bottom:
                pass
            elif distance_left_bottom < radius < distance_right_top:
                cnt[1] += 4
            else:
                cnt[0] += 4
    return cnt


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
