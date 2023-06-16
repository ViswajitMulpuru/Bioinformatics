import pandas as pd
df = pd.read_csv("AMP_frequency.csv", delimiter=",")
df1 = pd.read_csv("../B7A/AMP_frequency.csv", delimiter=",")
mid_res = pd.merge(df,df1,how='outer',on='Unnamed: 0')
mid_res.rename(columns = {'Genus_x':'B5B', 'Genus_y':'B7A'}, inplace = True)
df2 = pd.read_csv("../B27B/AMP_frequency.csv", delimiter=",")
mid_res1 = pd.merge(mid_res,df2,how='outer',on='Unnamed: 0')
mid_res1.rename(columns = {'Genus':'B27B'}, inplace = True)
