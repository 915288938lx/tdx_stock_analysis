import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(3,3),columns=list('abc'),index=list('ABC'))

print(df)
val = df.values
val_mat = df.as_matrix()
print('-----------------\n')
print(val)
print('val类型为:%s'%type(val))
val.sort()
val_mat.sort()
print(val_mat)
print(val)
# matrix = np.mat([[2,5,1],[4,6,2],[1,2,3]])
# print(matrix)
# matrix.sort()
# print(matrix)
#
