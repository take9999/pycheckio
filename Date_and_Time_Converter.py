def date_time(time: str) -> str:
    month_list = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]

    date_str, time_str = time.split(" ")
    day_int, month_int, year_int = map(int, date_str.split("."))
    hour_int, min_int = map(int, time_str.split(":"))

    unit_h_str = "hours" if hour_int != 1 else "hour"
    unit_m_str = "minutes" if min_int != 1 else "minute"

    ans = "{0} {1} {2} year {3} {4} {5} {6}".format(
        day_int,
        month_list[month_int - 1],
        year_int,
        hour_int,
        unit_h_str,
        min_int,
        unit_m_str
    )

    print(ans)

    return ans


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 01:01") == "20 November 1990 year 1 hour 1 minute", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
