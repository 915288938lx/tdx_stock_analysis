import numpy as np
# np.set_printoptions(threshold=np.inf)
import pandas as pd
header = ['user_id', 'item_id', 'rating', 'timestamp']

df = pd.read_csv('u.data', sep = '\t', names = header)
print(df)

# print(df['user_id'].max())
# print(df['item_id'].max())





n_users = df.user_id.unique().shape[0] #去重, 用户数

n_items = df.item_id.unique().shape[0]  #去重函数,电影数
print ('Number of users = ' + str(n_users) + ' | Number of movies = ' + str(n_items))


from sklearn import cross_validation as cv

train_data,test_data = cv.train_test_split(df, test_size = 0.25) # 这里是随机切的, 后面必须加上独热编码



train_data_matrix = np.zeros((n_users,n_items)) #用户数, 电影数组成的0填充矩阵

for line in train_data.itertuples():
    # print(line)
    # print(line[1],line[2])
    # print(line[3])
    # print(train_data_matrix[line[1]-1, line[2]-1])
    train_data_matrix[line[1]-1, line[2]-1] = line[3]

    # print(train_data_matrix)

test_data_matrix = np.zeros((n_users, n_items)) # 用户数, 电影数组成的0填充矩阵

for line in test_data.itertuples():

    test_data_matrix[line[1]-1, line[2]-1] = line[3]
# 计算余弦角度, 相关性

from sklearn.metrics.pairwise import pairwise_distances

user_similarity = pairwise_distances(train_data_matrix, metric = "cosine") #构造对称阵
item_similarity = pairwise_distances(train_data_matrix.T, metric = "cosine") # 构造对称阵

def predict(rating, similarity, type = 'user'):

    if type == 'user':

        mean_user_rating = rating.mean(axis = 1)

        rating_diff = (rating - mean_user_rating[:,np.newaxis])

        pred = mean_user_rating[:,np.newaxis] + similarity.dot(rating_diff) / np.array([np.abs(similarity).sum(axis=1)]).T

    elif type == 'item':

        pred = rating.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])

    return pred

item_prediction = predict(train_data_matrix, item_similarity, type = 'item')

user_prediction = predict(train_data_matrix, user_similarity, type = 'user')

from sklearn.metrics import mean_squared_error

from math import sqrt

def rmse(prediction, ground_truth):

    prediction = prediction[ground_truth.nonzero()].flatten()

    ground_truth = ground_truth[ground_truth.nonzero()].flatten()

    return sqrt(mean_squared_error(prediction, ground_truth))
print ('User based CF RMSE: ' + str(rmse(user_prediction, test_data_matrix)))

print ('Item based CF RMSe: ' + str(rmse(item_prediction, test_data_matrix)))
