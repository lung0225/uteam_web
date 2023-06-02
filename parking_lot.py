# limitation 

# 平日40 假日60
# 使用率和人流 的關係
# 使用率 參數

###### 討論
# 市調 變動時間區間
# 晚上 使用率高的停車塲 
import model 
import pandas as pd
### 
month_days = [31,30,31,30,31,30,31,31,30,31,30,31]
# data 1 : king_shuan
def load_data():
    king_shuan_total_xls = pd.ExcelFile("./king_shuan.xls")
    total_sum_up = pd.read_excel(king_shuan_total_xls, "總覽")
    print(total_sum_up)
    monthly_data = []
    for month in range(1,13):
        if month in [10,11,12]:
            monthly_data.append( pd.read_excel(king_shuan_total_xls, f"2022.{month}"))
        else:
            monthly_data.append( pd.read_excel(king_shuan_total_xls, f"2022.0{month}"))
    
    ################################# test 
    
    for i in range(0,12):
        print(f'{i+1} month data:')
        print(monthly_data[i].shape)
        print(monthly_data[i])
    
    #################################
class Data_set:
    def __init__(self,df) -> None:
        self.dataframe = df
    def extract_timely_data(self):
        df = self.dataframe.copy()
        column_names = self.dataframe.columns
        year_2022_data=[]
        
        for index in range(self.dataframe.shape[0]): # rows
            data = self.dataframe.iloc[index]
            for month in range(1,13):
                monthly_data = []
                for day in raneg(1,month_days[month]+1):
                    
                    monthly_data.append()
                year_2022_data.append(monthly_data)
            
'''
def main( now_use_rate ):
    if now_use_rate > pre:
        new_parameter = (now_use_rate - pre) *  average_stop_time
        model.add_parameter(new_parameter)
        new_price = prediction()
    else:
        new_parameter = (pre - now_use_rate) *  average_stop_time
        model.add_parameter(new_parameter)
        new_price = prediction()
'''
load_data()