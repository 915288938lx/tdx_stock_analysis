import pandas as pd, numpy as np
import os
import re
import time

class ready_to_pd:
    def get_iter_code_df(self,file_obj):
        if os.path.isfile(file_obj):
            # df = pd.read_csv(file_obj, encoding='gbk',usecols=[0])
            df = pd.read_csv(file_obj, encoding='gbk',names=['date', 'open', 'high', 'low', 'close', 'vol', 'money'],index_col=0)
            df.drop(df.index[df.shape[0] - 1], inplace=True)

            yield df
        else:
            for pwd, sub_dirs, files in os.walk(file_obj):

                for file in files:
                    li = []
                    code = re.findall('\d\d*', file)[0]
                    simple_name = file
                    full_name = file_obj + "/" + simple_name
                    df = pd.read_csv(full_name, encoding='gbk',names=['date', 'open', 'high', 'low', 'close', 'vol', 'money'],index_col=0)
                    df.drop(df.index[df.shape[0] - 1], inplace=True)
                    li.append(code)
                    li.append(df)

                    yield li


    def reindex_date(self,inx, df):
        df = df.reindex(inx)
        zvalues = df.loc[~(df.vol > 0)].loc[:, ['vol', 'money']]
        df.update(zvalues.fillna(0))
        df.fillna(method='ffill', inplace=True)
        return df



if __name__ == '__main__':

    today = time.localtime(time.time())
    today_str = time.strftime("%Y%m%d", today)+'.txt'
    print(today_str)

    ready = ready_to_pd()
    file_spec_0 = 'G:/zd_zszq/T0002/export/SZ#399300.csv' #沪深300指数
    # file_spec = 'SZ#000063.csv' # 中兴通讯
    file_obj = 'G:/zd_zszq/T0002/export'
    inx = next(ready.get_iter_code_df(file_spec_0)).index.values
    for li in ready.get_iter_code_df(file_obj):
        df = ready.reindex_date(inx, li[1])

        first =  df.ix[-1:,['close', 'vol']]
        second = df.ix[-2:-1,['close', 'vol']]
        third = df.ix[-3:-2,['close', 'vol']]
        a1 = first.values[0][1]
        a2 = second.values[0][1]*0.5

        aa = a1 < a2

        b1 = first.values[0][0]
        b2 = second.values[0][0]*0.98
        bb = b1 < b2
        if aa and bb:
            print(li[0])
            with open(today_str,'a') as f:
                f.write(li[0]+'\n')
        else:
            pass
        # print(li[0])
        # print(first)
        # print(second)
        # print(third)
        # print('\n\n\n')

    # zxtx = next(get_iter_code_df(file_spec)) #中心通讯额df
    # hssb = next(get_iter_code_df(file_spec_0)) #沪深300df
    #
    # hssb_date_index = hssb.index.values
    #
    # zxtx_ = zxtx.reindex(hssb_date_index)
    # zvalues = zxtx_.loc[~(zxtx_.vol > 0)].loc[:,['vol','money']]
    # zxtx_.update(zvalues.fillna(0))
    # zxtx_.fillna(method='ffill', inplace=True)
    # print(zxtx_)


