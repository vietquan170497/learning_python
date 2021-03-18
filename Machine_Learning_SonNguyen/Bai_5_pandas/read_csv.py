import pandas as pd
import numpy as np 

df = pd.read_csv('training-set.csv', header=0)

print(df['dur'])
# df=df[5]

# df.to_csv('vqn.csv')