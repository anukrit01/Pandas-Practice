import pandas as pd

a = pd.DataFrame({'key':['k0', 'k1', 'k2', 'k3'],
                  'A':['A0', 'A1', 'A2', 'A3'],
                  'B':['B0', 'B1', 'B2', 'B3']})
b = pd.DataFrame({'key':['k0', 'k1', 'k2', 'k3'],
                  'C':['C0', 'C1', 'C2', 'C3'],
                  'D':['D0', 'D1', 'D2', 'D3']})
print(pd.merge(a, b, on='key'))
'''
#Left Join
print(pd.merge(a, b, on='key', how='left'))
print(pd.merge(b, a, on='key', how='left'))

#Right Join
print(pd.merge(a, b, on='key', how='right'))
print(pd.merge(b, a, on='key', how='right'))
'''
#Outer Join
print(pd.merge(a, b, on='key', how='outer'))

#Inner Join
print(pd.merge(a, b, on='key', how='inner'))