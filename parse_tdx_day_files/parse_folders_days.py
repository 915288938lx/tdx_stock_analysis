import os
import re
from parse_tdx_day_files.parse_one_day import exactStock
folder = 'G:/zd_zszq/vipdoc/sh/lday'
# 获取文件夹下面所有"股票代码", "8个datas"
def get_iter_code_data(folder):
    for pwd, sub_dirs, files in os.walk(folder):
        for file in files:
            code = re.findall('\d\d*', file)[0]
            simple_name = file
            full_name = folder + "/" + simple_name
            data = exactStock(full_name)
            yield code,data

for i in get_iter_code_data(folder):
    print(i)