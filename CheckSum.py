def checkio(data):

    def remove_and_reverse(data):
        removed_str = ""
        for d in data:
            if d.isalpha() or d.isdigit():
                removed_str += d
        return reversed(removed_str)

    def reduced(num):
        if num < 10:
            return num
        else:
            str_num = str(num)
            return int(str_num[0]) + int(str_num[1])

    def odd_change(target):
        if target.isalpha():
            num = ord(target) - 48
        else:
            num = int(target)
        return num

    def even_change(target):
        if target.isalpha():
            num = ord(target) - 48
        else:
            num = int(target)
        return reduced(num*2)

    total = 0
    reversed_data = remove_and_reverse(data)
    for i, d in enumerate(reversed_data):
        if i % 2 == 0:  # even
            print(even_change(d))
            total += even_change(d)
        else:
            print(odd_change(d))
            total += odd_change(d)

    if (total % 10) == 0:
        ans = '0'
    else:
        ans = str(10 - (total%10))
    print("check sum:", ans, "total:", total)

    return [ans, total]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio("799 273 9871") == ["3", 67]), "First Test"
    assert (checkio("139-MT") == ["8", 52]), "Second Test"
    assert (checkio("123") == ["0", 10]), "Test for zero"
    assert (checkio("999_999") == ["6", 54]), "Third Test"
    assert (checkio("+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio("VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, done!")

