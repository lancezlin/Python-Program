
# coding: utf-8
# Author: Lance
# In[1]:

# Call Pandas and Numpy, set up work directory
import pandas as pd
import numpy as np
get_ipython().magic(u'cd "C:\\Users\\linla\\Documents\\Assignments\\R_SAS_Data"')


# In[11]:

# import the HPCO data (MayHpco) below:
MayHpco = pd.read_csv('heatmapHPCO.csv', sep=',', header=False)
# MayHpco


# In[24]:

# redefine country column:
# 1, US1-5 excl US3 to US_base, US3 to US_3
mayHpco = MayHpco.copy()
mayHpco.loc[:,'newCountryDesc']=mayHpco['Work Location Country Desc']
mayHpco.loc[(mayHpco['Salary Administration Plan Code'].isin(['US1','US2','US4','US5'])), 'newCountryDesc']='US_base'
mayHpco.loc[(mayHpco['Salary Administration Plan Code']=='US3'), 'newCountryDesc']='US_3'
# mayHpco
# 2, aggregate management level to 9 category
jobLevel = ['ADV','BAS','COR','ENT','EXP','INT','MAS','PRI','SEN','SPE','SU1','SU2','MG1','MG2','STR','FEL','DIR','VP','SFL','SVP','EVP','CEO']
jobLevelDic = {'ADV' : '9-Non-exempt','BAS' : '9-Non-exempt','COR' : '9-Non-exempt','ENT' : '8-ENT','EXP' : '5-EXP','INT' : '7-INT/SU1','MAS' : '4-MAS/MG1','PRI' : '9-Non-exempt','SEN' : '9-Non-exempt','SPE' : '6-SPE/SU2','SU1' : '7-INT/SU1','SU2' : '6-SPE/SU2','MG1' : '4-MAS/MG1','MG2' : '3-MG2','STR' : '2-DIR+','FEL' : '2-DIR+','DIR' : '2-DIR+','VP' : '1-VP+','SFL' : '1-VP+','SVP' : '1-VP+','EVP' : '1-VP+','CEO' : '0-CEO'}
for joblevel in jobLevel:
    mayHpco.loc[(mayHpco['Management Level']==joblevel), 'newJobLevel']=jobLevelDic[joblevel]
# mayHpco


# In[58]:

# calculation:
# 1, calculate US_base midpoint average
US_base = mayHpco.loc[(mayHpco['newCountryDesc']=='US_base')]
US_base_group = US_base.groupby(['Business Lvl 1 (Group) Desc', 'newJobLevel']).aggregate(np.mean)
US_base_avg = pd.DataFrame(US_base_group['Compensation Range - Midpoint (USD)']).reset_index()
# US_base_avg
# 2, merge back to rawdata
mayHpcoMerge = pd.merge(mayHpco, US_base_avg, how='left', on=['newJobLevel', 'Business Lvl 1 (Group) Desc'])
# mayHpcoMerge
# 3, index = Enployee(midpoint)/US_base_avg
mayHpcoMerge['costIndex']=100*mayHpcoMerge['Compensation Range - Midpoint (USD)_x']/mayHpcoMerge['Compensation Range - Midpoint (USD)_y']
mayHpcoMerge.to_csv('mayHpcoComplete.csv')


# In[59]:

# 1, calculate US_base average cost
US_base = mayHpco.loc[(mayHpco['newCountryDesc']=='US_base')]
US_base_group = US_base.groupby(['Business Lvl 1 (Group) Desc', 'newJobLevel']).aggregate(np.mean)
US_base_avg = pd.DataFrame(US_base_group['Primary Compensation Basis - Amount + PTB Rate (USD)']).reset_index()
#US_base_avg
# 2, merge back to rawdata
mayHpcoMerge = pd.merge(mayHpco, US_base_avg, how='left', on=['newJobLevel', 'Business Lvl 1 (Group) Desc'])
# mayHpcoMerge
# 3, index = Enployee(midpoint)/US_base_avg
mayHpcoMerge['costIndex']=100*mayHpcoMerge['Primary Compensation Basis - Amount + PTB Rate (USD)_x']/mayHpcoMerge['Primary Compensation Basis - Amount + PTB Rate (USD)_y']
mayHpcoMerge.to_csv('mayHpcoComplete2.csv')

