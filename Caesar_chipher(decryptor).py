def to_encrypt(text, delta):
    result_str = ""
    for t in text:
        if t == " ":
            result_str += t
        else:
            tmp_ord = ord(t) + delta
            if tmp_ord < 97:
                tmp_ord += 26
            elif tmp_ord > 122:
                tmp_ord -= 26
            result_str += chr(tmp_ord)
    return result_str


def to_decrypt(cryptotext, delta):
    dec_str = ""
    for text in cryptotext:
        if text.isalpha() or text == " ":
            dec_str += text

    cryptotext = to_encrypt(dec_str, delta)

    return cryptotext

if __name__ == '__main__':
    print("Example:")
    print(to_decrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_decrypt("!d! [e] &f*", -3) == "a b c"
    assert to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
    assert to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
    assert to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
    assert to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
    print("Coding complete? Click 'Check' to earn cool rewards!")

