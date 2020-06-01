import pandas as pd
import numpy as np

world_cup = {'Team':['West Indies', 'West Indies', 'India', 'Austrelia',
                    'Pakistan', 'Sri Lanka', 'Austrelia', 'Austrelia', 'Austrelia', 
                    'India', 'Austrelia'],
             'Rank':[7, 7, 2, 1, 6, 4, 1, 1, 1, 2, 1],
             'Year':[1975, 1979, 1983, 1987, 1992, 1996, 1999, 2003, 2007, 2011, 2015]}
#df = pd.DataFrame(world_cup)
'''
#print(df)
print(df.groupby('Team').groups)                #Groups of individual teams with correponding index no.
print(df.groupby(['Team', 'Rank']).groups)      #Grouped according to Team & Rank

for name, group in df.groupby('Team'):          #Iterating through groups
    print (name)
    print (group)
    print ('==============================')


df_grouped = df.groupby('Team')
print(df_grouped.get_group('India'))            #selecting a group using get_group()

print(df.groupby('Rank').groups)                #Aggregation
'''

#Concatenation
chokers = {'Team':['England', 'New Zealand', 'Zimbabwe'],
            'Rank':[3, 5, 9],
            'Year':[2019, 2022, 2025]}
df1 = pd.DataFrame(world_cup)
df2 = pd.DataFrame(chokers)
#print(pd.concat([df1, df2]))

#this can also be done as
print(df1.append(df2))
print(df2.append(df1))