from pickle import TRUE
import pandas as pd

# data = pd.Series([30,10,20])
#邏輯概念上 condition= [True, False,True]
#實際
# condition= data>5
# filteredData = data[condition]

# data= pd.DataFrame(dic)
# 篩選的都是列row 的資料
# 選出欄位 condition= data["column"]>5 

# data = pd.Series([30,15,20], index=['a','b','c'])
# condition= data >18
# filteredData= data[condition]
# print("篩選條件", condition, sep='\n')
# print(filteredData)

# data = pd.Series(['您好', 'Python', 'Pandas'])
# condition= data.str.contains('P')
# filteredData = data[condition]
# print("篩選條件", condition, sep='\n')
# print(filteredData)

data = pd.DataFrame({
    "name":["alan","jimmy","zac"],
    "salary":[30000,40000,50000]
}, index=["a","b","c"])
condition = data["salary"]>= 40000
condition1 = data["name"] == "alan"
filteredData = data[condition]
filteredData1= data[condition1]
print(condition1)
print(filteredData1)

