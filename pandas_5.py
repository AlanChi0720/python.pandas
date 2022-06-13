from ast import keyword
import pandas as pd

# 讀取資料 把CSV 讀成data frame
datacsv = "D:\python\python.pandas\googleplaystore.csv"
data = pd.read_csv(datacsv)

# 觀察資料
# print("data shape" ,data.shape)
# print("data columns", data.columns)
# print("======================")

# 分析資料1
# condition= data["Rating"] <=5
# data = data[condition]
# print("mean" ,data["Rating"].mean())
# print("median", data["Rating"].median())
# print("first 100 mean", 
#     data["Rating"].nlargest(1000).mean())

# 分析資料2
# data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]", "").replace("Free", ""))
# print('mean',data["Installs"].mean())
# condition= data["Installs"] >100000
# print('installs more than 100000', data[condition].shape[0])
# find error data spot: print(data.iloc[10472]) 

# application
keyword= input("plaese type keyword: ")
condition= data["App"].str.contains(keyword, case= False)
print("number of the search",data[condition]["App"].shape[0])
# contains("keyword", case= False) 忽略大小寫
