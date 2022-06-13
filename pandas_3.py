from sqlite3 import DatabaseError
import pandas as pd

#資料索引 pd.DataFrame(字典,index= 索引列表)
# index 為自訂 = 012345....
data = pd.DataFrame({
    "name":["alan","jimmy","zac"],
    "salary":[30000,40000,50000]
}, index=["a","b","c"])
# print("資料數量",data.size)
# print("資料形狀(列,欄)", data.shape)
# print("資料索引", data.index)
# print('get row', data.iloc[1], sep="\n")
# print('get row(index)', data.loc["a"], sep="\n")
# print('get column', data["name"], sep="\n" )

names= data["name"] # get Series data struc.
# print("upper caps all", names.str.upper(), sep="\n")
salaries= data["salary"]
# print('mean of salary', salaries.mean(), sep="\n")

data["revenue"]= [500000,400000,300000] #dtat[new name]= list
data['rank']= pd.Series([3,6,1], index=['a','b','c'])
data['cp']=data['revenue']/data['salary']

print(data)

