import pandas as pd, numpy as np
import os
import re
import time


def get_iter_code_df(file_obj):
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


def reindex_date(inx, df):
    df = df.reindex(inx)
    zvalues = df.loc[~(df.vol > 0)].loc[:, ['vol', 'money']]
    df.update(zvalues.fillna(0))
    df.fillna(method='ffill', inplace=True)
    return df



if __name__ == '__main__':


    file_spec_0 = 'G:/zd_zszq/T0002/export/SZ#399300.csv' #沪深300指数
    file_spec = 'SZ#000063.csv' # 中兴通讯
    df = get_iter_code_df(file_spec)
    df_ = next(df)
    idx = next(get_iter_code_df(file_spec_0)).index.values
    df__ = df_.reindex(idx)
    zvalues = df__.loc[~(df__.vol>=0)].loc[:,['vol','money']]
    zvalues_ = zvalues.fillna(0)
    df__.update(zvalues_)
    df__.fillna(method='ffill', inplace=True)
    print(df__)
    #
    # df__.update(zvalues.fillna(0))
    # df__.fillna(method='ffill', inplace=True)
    # print('\n\n\n')
    # print(df__)



