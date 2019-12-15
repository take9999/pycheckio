def prob(white, black, step):
    white_prob = white / (white+black)
    black_prob = 1 - white_prob

    if step == 1:
        return white_prob

    else:
        pick_white = white_prob * prob(white-1, black+1, step-1)
        pick_black = black_prob * prob(white+1, black-1, step-1)
        return pick_white + pick_black


def checkio(marbles, step):
    return round(prob(marbles.count('w'), marbles.count('b'), step), 2)


# below is wrong answer (round must last step only)
#
# def checkio(marbles: str, step: int) -> float:
#     str_size = len(marbles)
#     cnt_b = marbles.count("b")
#     cnt_w = marbles.count("w")
#     prob = 0.0
#
#     if step == 1:  # last_step return prob white
#         prob = cnt_w / str_size
#     else:
#         if cnt_b != 0 and cnt_w != 0:
#             new_marbles_w = "b" * (cnt_b+1) + "w" * (cnt_w-1)
#             new_marbles_b = "b" * (cnt_b-1) + "w" * (cnt_w+1)
#             prob = (cnt_b/str_size)*checkio(new_marbles_b, step-1) + (cnt_w/str_size)*checkio(new_marbles_w, step-1)
#         elif cnt_w == 0:
#             new_marbles_b = "b" * (cnt_b-1) + "w" * (cnt_w+1)
#             prob = (cnt_b/str_size)*checkio(new_marbles_b, step-1)
#         elif cnt_b == 0:
#             new_marbles_w = "b" * (cnt_b+1) + "w" * (cnt_w-1)
#             prob = (cnt_w/str_size)*checkio(new_marbles_w, step-1)
#     print(prob)
#     print(round(prob, 2))
#
#     return round(prob, 2)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio('bbw', 3))

    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
