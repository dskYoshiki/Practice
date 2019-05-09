import pandas as pd
import numpy
# Load training data
df = pd.read_csv("test.csv", header=0)

for i in range(len(df)):
    print("ix:" + df.ix[i, 'Name'])
    print("loc:" + df.loc[df.index[i], 'Name'])
# 列'Age'の要素がnullの行を削除,
# ただしindexは変わらないことに注意.
df_drp = df.dropna(subset=['Age'])
list_drp = list(df_drp.index)
print(pd.isnull(df.loc[df.index[10], 'Age']))
# 内包表記で, 列'Age'の要素がnullの行を抽出,
# 直接byteコードへ変換するため一番速い.
list_nan_com = [i for i in range(len(df_drp)) if pd.isnull(df.loc[df.index[i], 'Age'])]
print(list_nan_com)
# filterで, 列'Age'の要素がnullの行を抽出,
# listにする処理が意外と重いらしい?
list_nan_map = list(filter(lambda x: pd.isnull(df.loc[df.index[x], 'Age']), range(len(df_drp))))
print(list_nan_map)
for i in list_drp:
    print(i)
    print('ix:' + df.ix[i, 'Name'])
    print('loc:' + df.loc[df.index[i], 'Name'])

    print('Dix:' + df_drp.ix[i, 'Name'])
    print('Dloc:' + df_drp.loc[df.index[i], 'Name'])

# export result to be "titanic_submit.csv"
df.to_csv("result.csv")
df_drp.to_csv("result_drp.csv")