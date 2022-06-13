import pandas as pd

# Series
# data = pd.Series([20, 10, 15])
# max = data.max()
# median = data.median()
# data = data*2
# print(max, median)
# print(data)
# data = data == 20
# print(data)

#Data Frame
data = pd.DataFrame({
    "name":["alan", 'zac', 'jimmy'],
    "salary":[30000, 40000, 50000]
})
#取得特定欄位 column 直
column = data['salary']
#取得特定列 row 橫
row = data.iloc[0]

print(column,"\n",row)