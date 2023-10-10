import seaborn as sns
import pandas as pd
x=pd.read_csv("heatmap.csv")
#x.drop('Unnamed: 0.1', axis=1, inplace=True)
df=x.set_index('geneID')
#sns.heatmap(df)
#sns.set(rc={'figure.figsize':(20,10)})
sns.set(rc={'figure.figsize':(20,5)})
#colormap = sns.color_palette("Greens") 
#colormap = sns.color_palette("coolwarm") 
colormap = sns.color_palette("coolwarm", as_cmap=True) 
plot=sns.heatmap(df,annot=False, cmap=colormap)
#plot.figure(constrained_layout=True)
#plot.tight_layout()
#plot
fig=plot.get_figure()
fig.savefig("heatmap.pdf")
