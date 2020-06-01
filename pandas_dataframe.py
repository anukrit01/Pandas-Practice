import pandas
'''
#Creating a DataFrame (Converting a list into dataframe)
listx = [10,20,30,40,50]
table = pandas.DataFrame(listx)
print(table)


#Creating more than one Column with specific names
tab = [{'a':20, 'b':30}, {'a':15, 'b':20}, {'a':40, 'b':55}]
table = pandas.DataFrame(tab)
print(table)
'''
#Another way of doing the same and including index (Using Series)
data = {'One':pandas.Series([10,20,30], index=['a','b','c']),
        'Two':pandas.Series([15,25,35,45], index=['a','b','c','d'])}
table = pandas.DataFrame(data)
#print(table)


#Column Manipulations
table['Three'] = pandas.Series([50,60,70], index=['a','b','c'])   #New column addition
print(table)
'''
del(table['One'])   #Column deletion using del() function (Return not available here)
print(table)

print(table.pop('Two'))    #Column deletion using pop() function (Return available here)
print(table)
'''

#Row Manipulations
print(table.loc['c'])    #Row Selection (Location by row name)
print(table.iloc[1])     #(Location by row index)


table = table.append(pandas.DataFrame([[11,13], [17,19]], columns= ['Two', 'Three']))   #Row Addition
#print(table)

table = table.drop(0)    #Row Deletion
print(table)