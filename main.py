import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df_del=pd.read_csv("data/deliveries.csv")
df_mat=pd.read_csv("data/matches.csv")
#df_del.info()
df_mat.drop_duplicates(inplace=True)
print(f"Total Matches Played : {df_mat.shape[0]}")
def title(t:str):
    print(f"\t{"_"*61}\n\t\t\t{t}\n\t{"_"*61}")
def plotshow(label:list,title:str,dat:pd.Series):
    plt.figure(figsize=(19,20))
    dat.plot(kind='bar')
    plt.xlabel(label[0])
    plt.ylabel(label[1])
    plt.title(title)
    plt.savefig("img/"+title.replace(" ","_"))
#============= Matches Every Season =================#
t1="Matches Every Season"
title(t1)
season=df_mat.groupby("season").size()
print(season)
plotshow(["Season","Match"],t1,season)
#=============== Most Successful Teams =================#
t2="Total Number Matches Win By Team"
winners=df_mat['winner'].value_counts()
title(t2)
print(winners)
plotshow(["Team","Match"],t2,winners)
#================ Top Venues ==========================#
venue=df_mat['venue'].value_counts().sort_values(ascending=False)
t3="Top Venues"
title(t3)
print(venue)
plotshow(["Venue","Match"],t3,venue)
#================= Total Runs ==================#
total_run=df_del["total_runs"].sum()
print(f"Total Runs : {total_run}")
#================ Highest and Lowest Team Score ===========#
t4="Highest Team Score"
total_run=df_del.groupby(["match_id","batting_team","bowling_team"]
                     )["total_runs"].sum(
                         

                     ).sort_values()
title(t4)
print(total_run[:-11:-1])
t5="Lowest Team Score"
title(t5)
print(total_run[:15])
#=================== Highest of All Time =================#
orange=df_del.groupby(
'batter'
)['batsman_runs'].sum().sort_values(
ascending=False)
t6='Highest of All Time'
title(t6)
print(orange[:10])