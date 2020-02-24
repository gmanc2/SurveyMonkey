import pandas as pd
import numpy as np
import seaborn as sns
import excel2json
import matplotlib.pyplot as plt

# set plot style
plt.style.use('bmh')
df_1 = pd.read_csv('InitialPanel.csv', header=None, prefix='Q').iloc[2:]

df_1['group'] = 'group_1'

df_1.head()

excel2json.convert_from_file('InitialPanel.xlsx')