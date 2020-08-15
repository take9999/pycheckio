import re


def is_stressful(subj):
    red_words = ["h+e+l+p+", "a+s+a+p+", "u+r+g+e+n+t+"]
    lower_subj = subj.lower().replace("-", "").replace(".", "")

    # check 3 exclamation marks
    if len(lower_subj) >= 3:
        if "!!!" in lower_subj[-3:]:
            return True
    else:
        lower_subj = lower_subj.replace("!", "")

    # check is all upper
    if lower_subj != "":
        all_upper_flag = True
        for s in lower_subj:
            if s.islower:
                all_upper_flag = False
        if all_upper_flag is True:
            return True

    # check red words
    for rw in red_words:
        if re.search(rw, lower_subj):
            return True

    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
    print(is_stressful("where are you?!!!!"))
