import pandas as pd
from Compare import *
from scipy.spatial import distance
from sklearn.metrics.pairwise import cosine_similarity
from modify import yusado

name=input("궁금한 선수를 물어보세요 : ")
Player=playerCompare(name)
print("Physical\n",Player.physical(name).head(7),"\n")
print("Shooting\n",Player.shooting(name).head(7),"\n")
print("Link\n",Player.link(name).head(7),"\n")

Total=Player.physical(name).\
    merge(Player.shooting(name).iloc[:,[0,-1]],on="Player").\
    merge(Player.link(name).iloc[:,[0,-1]],on="Player")
Total.rename(columns={'Simi_x':'Physical', 'Simi_y':'Shooting','Simi':'Link'},inplace=True)
#
# Total['Similarity']=Total.apply(lambda x: distance.euclidean(x.loc['Physical':'Link']), axis=1)
#



print(yusado(Total).head(10))

pd.set_option('display.max_columns', 500)




