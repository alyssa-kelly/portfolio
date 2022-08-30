
import pandas as pd
import numpy as np

ama = pd.read_csv('/Users/alyssa/Desktop/data_analysis/project/rotten_tomatoes_amazon.csv')
net = pd.read_csv('/Users/alyssa/Desktop/data_analysis/project/rotten_tomatoes_netflix.csv')
dis = pd.read_csv('/Users/alyssa/Desktop/data_analysis/project/rotten_tomatoes_disney.csv')

all = pd.concat([ama, net, dis])
all.to_csv('/Users/alyssa/Desktop/data_analysis/project/rotten_all.csv', encoding='utf-8', index=False)
print('done')