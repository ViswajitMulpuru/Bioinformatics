import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
#df = pd.read_csv("amp_9.csv", usecols = ['Genus'], delimiter="\t")
df = pd.read_csv("amp_org.csv", usecols = ['Genus'], delimiter=" ")
print(df)

df['Genus'].value_counts().plot(ax=ax, kind='bar', xlabel='Genus', ylabel='AMPs')
df['Genus'].value_counts().to_csv('AMP_frequency.csv')
plt.savefig("AMP_freq_histo.png")
