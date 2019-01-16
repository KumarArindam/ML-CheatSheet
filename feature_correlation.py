## Removing the redundant features by comparing the correlation using Spearmans Rank correlation matrix

from scipy.cluster import hierarchy as hc

corr=np.round(scipy.stats.spearmanr(df_keep).correlation,4)
corr_condensed=hc.distance.squareform(1-corr)
z=hc.linkage(corr_condensed,method='average')
fig=plt.figure(figsize=(10,10))
dendogram=hc.dendogram(z,labels=df_keep.columns,orientation='left',leaf_font_size=16)
plt.show()