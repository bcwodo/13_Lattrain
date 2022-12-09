import pandas as pd
import numpy as np

df = pd.read_csv("vokabeln.csv")
#df["random"] = np.random.randn(df.shape[0])
#df.sort_values(["Kartei", "random"], ascending=False, inplace=True )
kartei = df.Kartei.value_counts()
print