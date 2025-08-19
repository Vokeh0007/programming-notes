import pandas as pd
import numpy as np

# ser = pd.Series()
# print("Pandas Series: ",ser)

# data = np.array(['g','h','j','k','l'])

# ser = pd.Series(data)
# print("Pandas Series:\n",ser)
# df = pd.DataFrame()
# print(df)

lst = ['Geeks','for','geeks','data','science','and','machine', 'learning']

df = pd.DataFrame(lst, columns=['W'])

print(df)
shoes=("balenciage","nike","adidas","puma","reebok")>>tuple
vehicles={"car":"toyota","bike":"honda","truck":"ford"}>>dict 