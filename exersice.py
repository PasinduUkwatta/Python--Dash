import numpy as np
import pandas as pd

number = np.arange(1,101)
print(number)

mat = number.reshape((20,5))
print(mat)


table =pd.DataFrame(mat)
table.columns = ['f1', 'f2','f3','f4','label']

print(table)


random_numbers =np.random.randint(0,100,(50,4))

col_names =['A','B','C','D',]

df = pd.DataFrame(data=random_numbers,columns=col_names)

print(df)