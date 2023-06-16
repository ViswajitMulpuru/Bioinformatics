from glob import glob
import pandas as pd

files = glob("/home/vis/Desktop/Vis/data/all_amp_freq_csv/*AMP*.csv")
x=files.pop()
y=files.pop()
df = pd.merge(
    pd.read_csv(x),
    pd.read_csv(y),
    how='outer',on='Unnamed: 0'
)
x1=x.split("/")
x2=x1[7].split("_")
x_name=str(x2[0])

y1=y.split("/")
y2=y1[7].split("_")
y_name=str(y2[0])
df.rename(columns = {'Genus_x':x_name, 'Genus_y':y_name}, inplace = True)
while files:
    z=files.pop()
    df = pd.merge(
        df, 
        pd.read_csv(z), 
        how='outer',on='Unnamed: 0'
    )
    z1=z.split("/")
    z2=z1[7].split("_")
    z_name=str(z2[0])
    df.rename(columns = {'Genus':z_name}, inplace = True)

df.to_csv("all_output.csv")


"""
import pandas as pd
df = pd.read_csv("AMP_frequency.csv", delimiter=",")
df1 = pd.read_csv("../B7A/AMP_frequency.csv", delimiter=",")
mid_res = pd.merge(df,df1,how='outer',on='Unnamed: 0')
mid_res.rename(columns = {'Genus_x':'B5B', 'Genus_y':'B7A'}, inplace = True)
df2 = pd.read_csv("../B27B/AMP_frequency.csv", delimiter=",")
mid_res1 = pd.merge(mid_res,df2,how='outer',on='Unnamed: 0')
mid_res1.rename(columns = {'Genus':'B27B'}, inplace = True)
"""
