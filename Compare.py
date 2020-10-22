from sklearn.preprocessing import RobustScaler
from sklearn.cluster import KMeans
from scipy.spatial import distance
from Robust import *
from modify import group, yusa, cleansing
import pandas as pd
class playerCompare:

    def __init__(self, Player):
        self.data = Player




    def physical(self,Player):


        Shot = pd.read_csv("C:/Users/USER/riyad/miru_soccer/Physical.csv")

        raw = Rbst("C:/Users/USER/riyad/miru_soccer/Physical.csv")

        Fw=cleansing(Shot,raw)

        pool = group(Fw)

        playerGroup = pool[pool['Player'].str.contains(Player)].iloc[0, 5]
        is_Group = pool['group'] == playerGroup
        spg = pool[is_Group]
        key = (spg[spg['Player'].str.contains(Player)].iloc[:, 3:5])
        bigyo = (spg.iloc[:, 3:5])

        return yusa(key, bigyo, spg)
    def shooting(selfself,Player):
        raw = Rbst("C:/Users/USER/riyad/miru_soccer/shooting.csv")

        Shot = pd.read_csv("C:/Users/USER/riyad/miru_soccer/shooting.csv")

        Shot.iloc[:, 3:] = raw.trans_rbst(raw.data)
        Fw = Shot[Shot['Pos'].str.contains('FW')]
        Fw = Fw.dropna(axis=0)

        pool = group(Fw)

        playerGroup = pool[pool['Player'].str.contains(Player)].iloc[0, 7]
        is_Group = pool['group'] == playerGroup
        spg = pool[is_Group]
        key = (spg[spg['Player'].str.contains(Player)].iloc[:, 3:7])
        bigyo = (spg.iloc[:, 3:7])

        return yusa(key, bigyo, spg)
    def link(self,Player):
        raw = Rbst("C:/Users/USER/riyad/miru_soccer/Link.csv")

        Shot = pd.read_csv("C:/Users/USER/riyad/miru_soccer/Link.csv")

        Shot.iloc[:, 3:] = raw.trans_rbst(raw.data)
        Fw = Shot[Shot['Pos'].str.contains('FW')]
        Fw = Fw.dropna(axis=0)

        pool = group(Fw)

        playerGroup = pool[pool['Player'].str.contains(Player)].iloc[0, 7]
        is_Group = pool['group'] == playerGroup
        spg = pool[is_Group]
        key = (spg[spg['Player'].str.contains(Player)].iloc[:, 3:7])
        bigyo = (spg.iloc[:, 3:7])

        return yusa(key, bigyo, spg)





