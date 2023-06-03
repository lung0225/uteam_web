
def time_calculater(month, day, hour , minute):
    month_table = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }
    sum_days = 0
    for i in range(1, int(month) ):
        sum_days = sum_days + month_table[i]
    return sum_days*60*24 + (int(day)-1)*24*60 + (int(hour)-1)*60 + int(minute)