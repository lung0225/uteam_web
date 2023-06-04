# limitation 

# 平日40 假日60
# 使用率和人流 的關係
# 使用率 參數

###### 討論
# 市調 變動時間區間
# 晚上 使用率高的停車塲 
import model 
import pandas as pd
from tools import time_calculater, graph_plot_year
from datetime import datetime
#import matplotlib.pyplot as plt

### 
month_days = [31,30,31,30,31,30,31,31,30,31,30,31]
monthly_data = []
# data 1 : king_shuan
def load_data():
    king_shuan_total_xls = pd.ExcelFile("./king_shuan.xls")
    total_sum_up = pd.read_excel(king_shuan_total_xls, "總覽")
    print(total_sum_up)
    for month in range(1,13):
        if month in [10,11,12]:
            monthly_data.append( pd.read_excel(king_shuan_total_xls, f"2022.{month}"))
        else:
            monthly_data.append( pd.read_excel(king_shuan_total_xls, f"2022.0{month}"))
    
  
def clean_data(): # clean duplicate data and 2021 data
    for i in range(len(monthly_data)):
        #dataframe = monthly_data[i]
        index = monthly_data[i].shape[0] - 1 
        monthly_data[i] = monthly_data[i].reset_index(drop=True)
        while pd.isnull(monthly_data[i].iloc[index][0]):
            monthly_data[i] = monthly_data[i].drop([index],axis=0).reset_index(drop=True)
            index = monthly_data[i].shape[0] - 1
            '''
    ################################# test 
    
    for i in range(0,12):
        print(f'{i+1} month data:')
        print(monthly_data[i].shape)
        print(monthly_data[i])
    #################################
              '''  
class Data_set:
    def __init__(self) -> None:
        self.all_data = monthly_data
        self.year_2022_data = [0 for i in range(525600)] # 60 * 24 * 365 february = 28
    def extract_timely_data(self):
        for dataframe in self.all_data:
        #dataframe = self.all_data[0]
            column_names = dataframe.columns
            for index in range(dataframe.shape[0]): # rows
                data = dataframe.iloc[index]
                #print(data)
                date_in = data[0] # timestamp
                time = data[1] # timestamp
                date_in = date_in.strftime("%d,%m,%Y")
                month = date_in[3:5]
                day = date_in[0:2]
                time = time.strftime("%H,%M,%S")
                hour = time[0:2]
                minute = time[3:5]
                in_time = time_calculater(month, day, hour, minute)
                ### 
                date_out = data[2]
                time = data[3]
                date_out = date_out.strftime("%d,%m,%Y")
                month = date_out[3:5]
                day = date_out[0:2]
                time = time.strftime("%H,%M,%S")
                hour = time[0:2]
                minute = time[3:5]
                out_time = time_calculater(month, day, hour, minute)
                for t in range(in_time , out_time+1):
                    self.year_2022_data[ t ] += 1
load_data()
clean_data()
king_shuan = Data_set()
king_shuan.extract_timely_data()
graph_plot_year(king_shuan.year_2022_data)

