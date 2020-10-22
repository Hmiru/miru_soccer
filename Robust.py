from sklearn.preprocessing import RobustScaler
from sklearn.cluster import KMeans
import pandas as pd
class Rbst:

    def __init__(self, stat):
        self.data = pd.read_csv(stat)
        self.data = self.data.iloc[:,3:]

        self.robusted = RobustScaler().fit(self.data)


    def trans_rbst(self,stat):
        new_stat=self.robusted.transform(stat)
        return pd.DataFrame(new_stat,columns = stat.columns)


