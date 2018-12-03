from recommend_system.recommend_sys import *
sparsity = round(1.0 - len(df) / float(n_users*n_items),3)

print ('The sparsity level of MovieLen100K is ' + str(sparsity * 100) + '%')

import scipy.sparse as sp

from scipy.sparse.linalg import svds #

u, s, vt = svds(train_data_matrix, k = 20)

s_diag_matrix = np.diag(s) # 对角化函数

x_pred = np.dot(np.dot(u,s_diag_matrix),vt)
rmse_ = rmse(x_pred, test_data_matrix)
print()