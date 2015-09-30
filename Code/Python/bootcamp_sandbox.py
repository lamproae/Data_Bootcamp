"""
Miscellaneous experiments for Data Bootcamp course   

Repository of materials (including this file): 
* https://github.com/DaveBackus/Data_Bootcamp/
* https://github.com/DaveBackus/Data_Bootcamp/Code/Python  

Written by Dave Backus, March 2015  
Created with Python 3.4 
"""
print('\nWelcome to Data Bootcamp!')

import datetime as dt 
print('Today is', dt.date.today())

"""
Check Python version 
"""
import sys

print('\nWhat version of Python are we running? \n', sys.version, '\n', sep='') 

if float(sys.version_info[0]) < 3.0:       
    raise Exception('Program halted, old version of Python. ' +  
                    'Sorry, you need to install Anaconda again.')
else:
    print('Congratulations, Python is up to date!')  
#    sys.exit(0)      # this halts execution

#%%    
"""
Assignments and copies 
http://stackoverflow.com/questions/10844493/dataframe-apply-in-python-pandas-alters-both-original-and-duplicate-dataframes
"""
# check 1
a = [1,2,3]
b = a
b[0] = 'WHOA!'
print('\nAfter assignment, a is', a)

# to make a copy 
a = [1,2,3]
b = a.copy()
b[0] = 'WHOA!' 
print('\nAfter copy, a is', a) 

# check 2
import numpy as np 
c = np.array([7, 3, 5]) 
d = c 
e = 2*c - 5
print('\nAfter assignment, (d, e) are', d, e)

c[0] = 10
print(d, e)

#%%    
"""
Check path of current working directory  
https://docs.python.org/2/library/os.path.html
"""
import os 

print('\nCurrent path:\n', os.getcwd(), sep='') 

"""
Check for specific file 
""" 
import os

print('\nList of files in working directory:')
[print(file) for file in os.listdir()]

file = 'SQL_support_code.py'
if not os.path.isfile(file):
    raise Exception('***** Program halted, file missing *****')
    
#%%    
"""
IMF's historical database on public debt 
https://www.imf.org/External/pubs/cat/longres.aspx?sk=24332.0
rows are countries, columns are dates (1692-2012) 
"""
import pandas as pd 
import urllib              # handles internet files 
import zipfile             # handles zip files 
import os 

# copy zip file to hard drive 
print('\nCopy IMF historical debt data to hard drive')
url = 'https://www.imf.org/external/pubs/ft/wp/2010/Data/wp10245.zip'
zname = '../Temp/' + os.path.basename(url)   # strip out file name 
urllib.request.urlretrieve(url, zname)       # copy file from url to disk 

# extract spreadsheet in two steps
zf = zipfile.ZipFile(zname, 'r')
zf.printdir()
xlsname = zf.namelist()[0]
xls = zf.extract(xlsname)

df = pd.read_excel(xls, sheetname=1, na_values=['…', '….', ''], index_col=0, 
                   encoding='utf-8') 

print('Type: ', type(df))
print('Shape (dimensions): ', df.shape)
print('Column labels (variables): ', df.columns.tolist()) 
print('Variable types: \n', df.dtypes, sep='')

df.tail()

#%%
# select years 1980 to 2013 and ifscode 
years = [year for year in range(1980, 2013)]
years_str = [str(year) for year in years]
vars = ['ifscode'] + years

some = df[vars]

#%%
"""
Shortcut:  save file to disk, read from there 
"""
file = '../Temp/' + 'Debt Database Fall 2013 Vintage.xlsx' 
df = pd.read_excel(file, sheetname=1, na_values=['…', '….', ''], index_col=0, 
                   encoding='utf-8') 
#%%
print('Type: ', type(df))
print('Shape (dimensions): ', df.shape)
print('Column labels (variables): ', df.columns.tolist()) 
print('Variable types: \n', df.dtypes, sep='')

# select years 1980 to 2013 and ifscode 
years = [year for year in range(1980, 2013)]
#years_str = [str(year) for year in years]
vars = years
some = df[vars]



#%%
"""
unicode
http://eev.ee/blog/2015/09/12/dark-corners-of-unicode/
https://docs.python.org/3.4/library/unicodedata.html 
https://docs.python.org/3/howto/unicode.html#unicode-properties
http://stackoverflow.com/questions/508558/what-charset-does-microsoft-excel-use-when-saving-files
"""
import unicodedata 

# this came up in the IMF debt data (cut and paste from spreadsheet)
s = '…'
len(s)

print('Unicode category and name: ', 
      unicodedata.category(s), ', ', unicodedata.name(s), sep='') 
 

#%%
"""
urrlib version of data input from csv 
"""
# copy file from url to hard drive 
import urllib.request           
file = 'foo.csv'
url1 = 'https://raw.githubusercontent.com/DaveBackus/Data_Bootcamp/master/'
url2 = 'Code/Data/test1.csv'
url = url1 + url2 
urllib.request.urlretrieve(url, file)

# Sarah's version 
f = urllib.request.urlopen(url)
file = 'foo_sbh.csv'
with open(file, 'wb') as local_file:
    local_file.write(f.read())

#%%
"""
World Bank WDI from zip file 
File is too big, takes too long to read in class (but great stuff!) 
"""
import pandas as pd
import urllib
import zipfile
import os 

# this is a big file, best to test with something smaller 
url  = 'http://databank.worldbank.org/data/download/WDI_csv.zip'
file = '../Temp/' + os.path.basename(url)   # strip out file name 
urllib.request.urlretrieve(url, file)        # copy to disk 

# see what's there
print(['Is zipfile?', zipfile.is_zipfile(file)])
zf = zipfile.ZipFile(file, 'r')
#print('List of zipfile contents (two versions)')
zf.printdir()

# extract a component 
csv = zf.extract('WDI_Data.csv')        # copy to disk  
df1 = pd.read_csv(csv)       # read
print(df1.columns)                      # check contents 

# alternative:  open and read
csv = zf.open('WDI_Data.csv')
df2 = pd.read_csv(csv)
print(df2.columns)


#%%
"""
Penn World Table
http://www.rug.nl/research/ggdc/data/pwt/pwt-8.1
Takes about 10 seconds on home wireless network  
"""
import pandas as pd

url = 'http://www.rug.nl/research/ggdc/data/pwt/v81/pwt81.xlsx'
df = pd.read_excel(url, sheetname=2)

print(df.ftypes)

#%%
"""
Maddison data 
http://www.ggdc.net/maddison/maddison-project/home.htm
Takes about 10 seconds on home wireless network  
"""
import pandas as pd

url = 'http://www.ggdc.net/maddison/maddison-project/data/mpd_2013-01.xlsx'
df = pd.read_excel(url) #, skiprows=1, index_col=0)

print(df.ftypes)

#%%
"""
Equality of Opportunity 
http://www.equality-of-opportunity.org/index.php/data 
"""
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib as mpl 

url = 'http://www.equality-of-opportunity.org/images/online_data_tables.xls'
df = pd.read_excel(url, sheetname=1, skiprows=8, header=0, index_col=0)
print(df.tail())
df.tail()
#%%

# fix column labels
df.columns = [pct for pct in range(1, 101)]
print('\n', df.ftypes[0:7], sep='')

# trim to eliminate extremes 
trimmed = df.iloc[6:92, 6:92]

#http://stackoverflow.com/questions/14391959/heatmap-in-matplotlib-with-pcolor 
fig, ax = plt.subplots()
heatmap = ax.pcolor(trimmed, cmap=plt.cm.Blues)