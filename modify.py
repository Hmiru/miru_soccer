from sklearn import datasets
from scipy.spatial import distance
import pandas as pd
from sklearn.cluster import KMeans

def cleansing(a,b):
    a.iloc[:, 3:] = b.trans_rbst(b.data)
    Fw = a[a['Pos'].str.contains('FW')]
    Fw = Fw.dropna(axis=0)
    return Fw

def group(a):
    feature=a.iloc[:, 3:]
    model = KMeans(n_clusters=2, algorithm='auto')
    model.fit(feature)
    predict = pd.DataFrame(model.predict(feature))
    predict.columns = ['group']
    grouped = pd.concat([a.reset_index(drop=True), predict], axis=1)
    return grouped


def yusa(a, b, c):
    dist = []
    for i in range(0, len(b)):
        dist.append(distance.euclidean(
            [a.iloc[0, 0:]], [b.iloc[i, 0:]]))
    c = c.assign(Simi=dist)
    return pd.DataFrame(c.iloc[:,[0,2,-1]].sort_values(by=['Simi'], axis=0).round(2))

def yusado(a):
    dist = []
    for i in range(0, len(a)):
        dist.append(distance.euclidean(
            [a.iloc[0, 2:]], [a.iloc[i, 2:]]))
    a = a.assign(Simi=dist)
    return pd.DataFrame(a.sort_values(by=['Simi'], axis=0).round(2))