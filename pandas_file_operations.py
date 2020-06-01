import pandas
'''
#Loading and Storing of CSV data file into DataFrames

table = pandas.read_csv('my_file.csv')  #Loading into dataframes
print(table)

table.to_csv('newfile.csv')  #Storing data into CSV file
'''

#Loading and Storing of Excelsheet data
sheet = pandas.read_excel("dataset.xlsx")
print(sheet)

sheet.to_excel('dataset.xlsx')