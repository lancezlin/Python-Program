
# coding: utf-8

# In[17]:

# Call Pandas and Numpy, set up work directory
import pandas as pd
import numpy as np
get_ipython().magic(u'cd "C:\\Users\\linla\\Documents\\Assignments\\R_SAS_Data"')


# In[18]:

readIn = ['histMgt14.csv', 'histMgt13.csv', 'histMgt12.csv', 'histMgt11.csv', 'histMgt10.csv']
parentData = pd.read_csv('mg12_jul15.csv', header=False, sep=',')
mgt_dic = {'ADV' : 1, 
           'COR' : 1, 
           'ENT' : 1, 
           'INT' : 1, 
           'DIR' : 4, 
           'MG3' : 4, 
           'STR' : 4, 
           'MG2' : 3, 
           'MAS' : 1, 
           'MG1' : 2, 
           'EXP' : 1,
           'PRI' : 1,
           'SPE' : 1,
           'SU1' : 1,
           'SU2' : 1,
           'SEN' : 1,
           'BAS' : 1,
           '' : 0
               }
for mgt in mgt_dic.keys():
    parentData.loc[parentData['Management Level']==mgt, 'MGT Score']=mgt_dic[mgt]


# In[19]:

def dataMerge(mergeList, parentFile):
    # endFile = pd.dataframe()
    for mFile in mergeList:
        childFile = pd.read_csv(mFile, sep=',', header=False)
        for mgt in mgt_dic.keys():
            childFile.loc[childFile['Management Level']==mgt, 'MGT Score'] = mgt_dic[mgt]
        parentFile = pd.merge(parentFile, childFile, how='left', on='Worker ID')
    return parentFile


# In[20]:

endFile = dataMerge(readIn, parentData)
endFile.to_csv('mg12Merged.csv')

