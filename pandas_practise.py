import pandas as pd

df = pd.read_csv('salaries.csv')

print(df)

#when we get more than one column we need to define them in list , separatly
print(df[['Name','Salary']])
print(df['Salary'].min())
print(df['Salary'].mean())


age_critira =df['Age']>30

print(age_critira)

#this will produce the results that satisfying the needed condition
print(df[age_critira])

print(df[df['Age']>30])

#this will produce all the calculations
print(df.describe())