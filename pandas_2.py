import pandas as pd

# 以列表資料為底, 建立Series
#pd.Series(列表資料, index= 索引列表)

data = pd.Series([3,10,20,5,-12] , index=['a','b','c','d','e'])
# 資料的索引 依據索引取得資料
# print(data.index, data["a"])
# 所有乘法的總和 
# print(data.prod())
# #取前三大 取前二小 
# print(data.nlargest(3),'\n',data.nsmallest(2))

# str 各種操作
data = pd.Series(['您好', 'Python', 'Pandas'])
# 以 , 串起每個資料
# print(data.str.cat(sep=','))
# # 判斷字串是否包含P (大小寫有分)
# print(data.str.contains('P'))
# print(data.str.replace('您好', 'Hello'))
print(data.str.upper(), sep="\n")