import matplotlib.pyplot as plt
import pandas as pd 
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
def time_calculater(month, day, hour , minute):
    
    sum_days = 0
    for i in range(1, int(month) ):
        sum_days = sum_days + month_table[i]
    return sum_days*60*24 + (int(day)-1)*24*60 + (int(hour))*60 + int(minute)
def month_time_cal(month):
    start_time = time_calculater(month,1,0,0)
    end_time = time_calculater(month, month_table[month],23 ,59)
    return start_time, end_time
def graph_plot_year(data):
    for month in range(1,13):
        month_date = month_table[month]
        time_series = pd.date_range(f"2022-{month}-01 00:00:00",f"2022-{month}-{month_date} 23:59:00",freq='1min' )
        start,end = month_time_cal(month)
        print(start)
        print(end)
        plt.figure(figsize=(20,20))
        plt.title(f"m{month}_use_rate")
        plt.plot(time_series,data[start:end+1])
        plt.savefig(f'./graphs/m{month}_use_rate.png')
        plt.show()
        