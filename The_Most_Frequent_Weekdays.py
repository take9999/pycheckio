import datetime
from calendar import monthrange


# other solution
def most_frequent_days(a):
    # your code here
    from calendar import weekday,day_name
    return [day_name[i] for i in sorted({weekday(a,1,1),weekday(a,12,31)})]


def get_most_frequent_weekdays(year_data):
    # count for each weekday
    cnt_monday = 0
    cnt_tuesday = 0
    cnt_wednesday = 0
    cnt_thursday = 0
    cnt_friday = 0
    cnt_saturday = 0
    cnt_sunday = 0

    # weekdays string
    dict_weekdays_name = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

    for month_data in range(1, 13):
        # 月末日の取得
        _, lastDay = monthrange(int(year_data), int(month_data))

        # 1ヶ月分のカウント
        for dayNum in range(lastDay):
            if datetime.datetime(int(year_data), int(month_data), dayNum + 1).weekday() == 0:
                cnt_monday += 1
            elif datetime.datetime(int(year_data), int(month_data), dayNum + 1).weekday() == 1:
                cnt_tuesday += 1
            elif datetime.datetime(int(year_data), int(month_data), dayNum + 1).weekday() == 2:
                cnt_wednesday += 1
            elif datetime.datetime(int(year_data), int(month_data), dayNum + 1).weekday() == 3:
                cnt_thursday += 1
            elif datetime.datetime(int(year_data), int(month_data), dayNum + 1).weekday() == 4:
                cnt_friday += 1
            elif datetime.datetime(int(year_data), int(month_data), dayNum + 1).weekday() == 5:
                cnt_saturday += 1
            else:
                cnt_sunday += 1

    # print(cnt_monday, cnt_tuesday, cnt_wednesday, cnt_thursday, cnt_friday, cnt_saturday, cnt_sunday)
    weekdays_freq_list = [cnt_monday, cnt_tuesday, cnt_wednesday, cnt_thursday, cnt_friday, cnt_saturday, cnt_sunday]

    max_freq_idx_list = [i for i, v in enumerate(weekdays_freq_list) if v == max(weekdays_freq_list)]
    # print(max_freq_idx_list)

    return [dict_weekdays_name[x] for x in max_freq_idx_list]


print(get_most_frequent_weekdays(1084))
