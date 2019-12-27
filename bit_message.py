import datetime

def checkio(data):
    def get_octet(octet):
        return int(data[octet * 2:octet * 2 + 2], 16)

    def get_type(octet=0):
        type_value = (get_octet(octet) & int('00001100', 2)) >> 2
        return [7, 8, 16][type_value]  # 0: 7bit, 1: 8bit, 2: 16bit

    def get_time(octet):
        return int(data[octet * 2:octet * 2 + 2][::-1], 10)

    def get_tz(octet=7):
        o = get_octet(octet)
        sign = -1 if o & int('00001000', 2) else 1
        num = (o & int('00000111', 2)) * 10 + ((o & int('11110000', 2)) >> 4)
        return sign * num * 15 // 60

    def get_length(octet=8):
        return get_octet(octet)

    data = data.strip()

    # timestamp
    year = get_time(1)
    year += 2000 if year < 70 else 1900
    d = datetime.datetime(year, get_time(2), get_time(3), get_time(4), get_time(5), get_time(6))
    timestamp = d.strftime('%d %b %Y %H:%M:%S') + ' GMT {0:+d}'.format(get_tz())

    # message
    bit_length = get_type()
    message = ''
    message_data = data[9 * 2:]
    if bit_length == 7:  # 7bit
        reversed_data = ''.join(a + b for a, b in zip(message_data[-2::-2], message_data[-1::-2]))
        reversed_bits = ''.join([format(int(c, 16), '04b') for c in reversed_data])
        for i in range(len(reversed_bits) - 7, -1, -7):
            message += chr(int(reversed_bits[i:i + 7], 2))
    else:
        # 8bit/16bit
        char_size = bit_length // 4
        for i in range(0, len(message_data), char_size):
            message += chr(int(message_data[i:i + char_size], 16))

    l = get_length()
    return [timestamp, l, message[:l]]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio('002080629173148007EDF27C1E3E9701') ==
            ['26 Aug 2002 19:37:41 GMT +2', 7, 'message']), "First Test"

    assert (checkio('00317050201171820FD3323BDC0ED341C4303DEC3E8700') ==
            ['05 Jul 2013 02:11:17 GMT +7', 15, 'Selamat Datang!']), "Second Test, 7 bit"

    assert (checkio('000130925161956915C8729E054A82C26D50DA0D7296EFA0EC5BBE06') ==
            ['29 Mar 2010 15:16:59 GMT -4', 21, 'Hey, I am in New York']), "Third Test, negative timezone"

    assert (checkio('08071010101010611F04180441043A043B044E04470435043D043804350020043F043E04340442043204350440043604340430043504420020043F0440043004320438043B043E') ==
            ['01 Jan 1970 01:01:01 GMT +4', 31,
             'Исключение подтверждает правило']), "Fourth Test, simulate 32-bit signed integer real life problem"

    assert (checkio('088310913041804C23805E4E0D82E5805E4E4B002C805E4E4B4E0D82E5898B4E4B002C898B4E4B4E0D82E577E54E4B002C77E54E4B4E0D82E5884C4E4B002C5B7881F365BC884C4E4B800C6B6277E3 ') ==
            ['19 Jan 2038 03:14:08 GMT -11', 35, '聞不若聞之,聞之不若見之,見之不若知之,知之不若行之,學至於行之而止矣']), "But, we pass Y2K38 problem"

