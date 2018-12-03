import numpy as np
import pandas as pd
# df = pd.read_csv('SZ#002422.csv',encoding='gbk',names=['date', 'open', 'high', 'low', 'close', 'vol', 'money'])
# df.drop(df.index[df.shape[0] - 1], inplace=True)
# # print(df)
# n_users = df.date.unique().shape[0] # 行数
# print(n_users) # 19
#
# n_items = 10  #列数
# print(n_items)
#
# from sklearn import cross_validation as cv
#
# train_data,test_data = cv.train_test_split(df, test_size = 0.25)
# print(train_data)
#
# train_data_matrix = np.zeros((n_users,n_items))
# print(train_data_matrix)#用户数, 电影数组成的0填充矩阵
# for line in train_data.itertuples():
#     print(line)
#
#     train_data_matrix[line[1], line[2]] = line[3]
#     print(train_data_matrix)



x = np.arange(3)
print(x)
y = x[:,np.newaxis]
print(y)






# train_data_matrix = np.zeros((n_users,n_items)) #用户数, 电影数组成的0填充矩阵
#

# for line in train_data.itertuples():
#
#     train_data_matrix[line[1]-1, line[2]-1] = line[3]
#     print(train_data_matrix)
