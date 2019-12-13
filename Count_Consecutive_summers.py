def count_consecutive_summers(num):
    result = []
    result.append([num])

    for_end_num = (num // 2 + 1)

    for i in range(1, for_end_num+1):
        for j in range(i+1, for_end_num+1):
            sum_i2j = int((i+j) * (j-(i-1)) / 2)
            if sum_i2j > num:
                break
            elif sum_i2j == num:
                result.append(([x for x in range(i, j)]))
    print(result)
    return len(result)


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
