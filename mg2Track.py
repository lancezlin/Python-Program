
# coding: utf-8

# ** Step 1: # Call Pandas and Numpy, set up work directory **

# In[22]:

# Call Pandas and Numpy, set up work directory
import pandas as pd
import numpy as np
get_ipython().magic(u'cd "C:\\Users\\linla\\Documents\\Assignments\\R_SAS_Data"')


# **Step 2: # Read raw data from Local Directory and store it in 'rawdata' **

# In[23]:

rawdata = pd.read_csv("NewOrg_Q3.csv", sep=',', header=False)
julOds = pd.read_csv("julOds.csv", sep=',', header=False)
rawdata1 = pd.merge(rawdata, julOds, how='left', on= 'Worker ID')
rawdata2 = rawdata1.loc[rawdata1['HPEI']=='HPE']
# rawdata.head(5)
# rawdata.columns
len(rawdata2)


# ** ######## Setting variables shortcuts **

# In[24]:

x = rawdata2.copy()
pf = 'Preferred Name'
y = 'Business Lvl 2 (Unit) Desc'
z = 'Management Chain - Level 01 Preferred Name'
zz = 'Management Chain - Level 02 Preferred Name'
b1c = 'Business Lvl 1 (Group) Code'
b2c = 'Business Lvl 2 (Unit) Code'
l1 = 'Business Lvl 1 (Group) Desc'
l3 = 'Business Lvl 3 (Org Chart) Desc'
p_index = ['Management Level']
p_values = ['Primary Compensation Basis - Amount + PTB Rate (USD)', 'Worker ID']
p_columns1 = ['Business Lvl 1 (Group) Code']
p_columns2 = ['Business Lvl 2 (Unit) Code']
mgt_lvl = ['EVP', 'SVP', 'VP', 'SFL', 'DIR', 'FEL', 'STR', 'MG2']


# **Step 2.5 PPS related adjustments**

# In[25]:

hpe_pps_l1 = [
XXX
XXX
]
hpe_pps_dic1 = {
XXX : XXX
XXX : XXX
}# <-- L1 leaders : L1 orgs


# In[26]:

hpe_pps_l2 = [
XXX
XXX
]
hpe_pps_dic2 = {
XXX : XXX
XXX : XXX
}


# In[27]:

for ppsL1 in hpe_pps_l1:
    x.loc[(x[l1]=='Printing and Personal System') & (x['FutureL1']==ppsL1), b1c]=hpe_pps_dic1[ppsL1]
    x.loc[(x[y].str.startswith('PPS', na=False)) & (x['FutureL1']==ppsL1), b1c]=hpe_pps_dic1[ppsL1]
for ppsL2 in hpe_pps_l2:
    x.loc[(x[l1]=='Printing and Personal System') & (x['FutureL2']==ppsL2), b2c]=hpe_pps_dic2[ppsL2]
    x.loc[(x[y].str.startswith('PPS', na=False)) & (x['FutureL2']==ppsL2), b2c]=hpe_pps_dic2[ppsL2]


# ** Step 3: # Adjust Foreign Service Expats to align each L1 org based on Management Hierarchy**

# In[28]:

'''
def OFS(x, y, z, b1c):
    x.loc[(x[y]=='Foreign Service Expats') & (x[z]=='Neri, Antonio F'), b1c]='EGR'
    return x
    
t = OFS(rawdata, 'Business Lvl 2 (Unit) Desc', 'Management Chain - Level 01 Preferred Name', 'Business Lvl 1 (Group) Code')
print t

'''

x.loc[(x[y]=='Foreign Service Expats') & (x[z]=='Ne'), b1c]='EGR'
x.loc[(x[y]=='Foreign Service Expats') & (x[z]=='Fi'), b1c]='LAB'
x.loc[(x[y]=='Foreign Service Expats') & (x[z]=='Go'), b1c]='CMP'
x.loc[(x[y]=='Foreign Service Expats') & (x[z]=='Hi'), b1c]='CCO&TNO'
x.loc[(x[y]=='Foreign Service Expats') & (x[z]=='Ke'), b1c]='HR'
x.loc[(x[y]=='Foreign Service Expats') & (x[z]=='Le'), b1c]='FIN'
x.loc[(x[y]=='Foreign Service Expats') & (x[z]=='Ne'), b1c]='ESHP'
x.loc[(x[y]=='Foreign Service Expats') & (x[z]=='SF'), b1c]='LEGO'
x.loc[(x[y]=='Foreign Service Expats') & (x[z]=='Yt'), b1c]='SWHP'
x.loc[(x[y]=='Foreign Service Expats') & (x[z]=='Hl'), b1c]='OP_SMO'

# x.loc[x[y]=='Foreign Service Expats']
# x.to_csv('checkpoint3.csv')
# y[(y['Business Lvl 2 (Unit) Desc']=='Foreign Service Expats') & (y['Management Chain - Level 01 Preferred Name']=='Neri Antonio F')]


# ** Step 4: #   Adjust Foreign Service Expats to align each L2 org based on Management Hierarchy **

# In[29]:

ofs_lib = [
XXX
XXX
]
ofs_dic = {
XXX : XXX
XXX : XXX
}

for zzz in ofs_lib:
    x.loc[(x[y]=='Foreign Service Expats') & (x[zz]==zzz), b2c]=ofs_dic[zzz]
    x.loc[(x[y]=='Foreign Service Expats') & (x['Preferred Name']==zzz), b2c]=ofs_dic[zzz]
# x.loc[x[y]=='Foreign Service Expats']
# x.to_csv('checkpoint4.csv')


# ** Step 5: # Align "Seperation" back to their original L2 Orgs **

# In[30]:

sep_dic = {
XXX : XXX
XXX : XXX
}
sep_lib = [
XXX
XXX
]

for zzz in sep_lib:
    x.loc[(x[y]=='Separation') & (x[zz]==zzz), b2c]=sep_dic[zzz]
    
# for those L2 leader themselves:
for zzz in sep_lib:
    x.loc[(x[y]=='Separation') & (x['Preferred Name']==zzz), b2c]=sep_dic[zzz]
# x.loc[x[y]=='Separation']
# x.to_csv('checkpoint5.csv')


# ** Step 6: # Align Seperation back to their original L1 Orgs **

# In[31]:

x.loc[(x[y]=='Separation') & (x[z]=='Ne'), b1c]='EGR'
x.loc[(x[y]=='Separation') & (x[z]=='Ve'), b1c]='EGR'
x.loc[(x[y]=='Separation') & (x[z]=='FR'), b1c]='CLU'
x.loc[(x[y]=='Separation') & (x[z]=='Go'), b1c]='CMP'
x.loc[(x[y]=='Separation') & (x[z]=='Hn'), b1c]='TNO'
x.loc[(x[y]=='Separation') & (x[z]=='Ke'), b1c]='HR'
x.loc[(x[y]=='Separation') & (x[z]=='Le'), b1c]='FIN'
x.loc[(x[y]=='Separation') & (x[z]=='Ne'), b1c]='ESHP'
x.loc[(x[y]=='Separation') & (x[z]=='SF'), b1c]='LEGO'
x.loc[(x[y]=='Separation') & (x[z]=='Yt'), b1c]='SWHP'
x.loc[(x[y]=='Separation') & (x[z]=='Hs'), b1c]='OP_SMO'
# tag XX to CSOF/EGR as L1
x.loc[(x[y]=='Separation') & (x[z]=='Mm'), b1c]='CSOF'
x.loc[(x[y]=='Separation') & (x[z]=='Mm'), l3]='Corporate Strategy'
x.loc[(x[y]=='Separation') & (x['Preferred Name']=='Mm'), b1c]='CSOF'
x.loc[(x[y]=='Separation') & (x['Preferred Name']=='Mm'), l3]='Corporate Strategy'
x.loc[(x[y]=='Separation') & (x['Preferred Name']=='ll'), b1c]='EGR'

# x.to_csv('checkpoint6.csv')


# ** Step 7: # Align who report into Hs to CCO&TNO as L1 org **

#                                         **# Adjust the L2 based on the management hierarchy **

# In[32]:

tno_lib = [
XXX
XXX
]
tno_dic = {
 # Align those to distinct PHP within CCO&TNO
 # Align those to distinct PHP within CCO&TNO
XXX : XXX
XXX : XXX # Align those to distinct PHP within CCO&TNO
}
x.loc[(x[z]=='HJ')|(x['Preferred Name']=='HJ'), b1c]='CCO&TNO'

for zzz in tno_lib:
    x.loc[(x[z]=='HJ') & (x[zz]==zzz), b2c]=tno_dic[zzz]
    x.loc[(x[z]=='HJ') & (x['Preferred Name']==zzz), b2c]=tno_dic[zzz]
    
# Customer Advocacy team setting up
x.loc[(x[z]=='Hn') & (x[zz]=='BR'), b1c]='CCO&TNO'
x.loc[(x[zz]=='BR'), b2c]='CIO TBD'
# x.loc[(x['Management Chain - Level 03 Preferred Name']=='RK'), b1c]='CCO&TNO'
x.loc[(x['Management Chain - Level 03 Preferred Name']=='PH'), b2c]='Customer Advocacy' 
x.loc[(x['Management Chain - Level 03 Preferred Name']=='GL'), b2c]='Customer Advocacy' # name changed since Jul
ca_lib = [
XXX
XXX
]
for zzz in ca_lib:
    x.loc[(x['Preferred Name']==zzz), b1c]='CCO&TNO'
    x.loc[(x['Preferred Name']==zzz), b2c]='Customer Advocacy'

# x.to_csv('checkpoint7.csv')


# ** Step 8: # Ch's organization - OP_SMO alignments **

# In[33]:

x.loc[(x[z]=='Hl'), b1c]='OP_SMO' # All people report through Hsu aligned to OP_SMO
x.loc[(x['Preferred Name']=='Hl'), b1c]='OP_SMO' #Ky & Only H themselves to OP_SMO
x.loc[(x['Preferred Name']=='Hl'),b2c]='Others'
# OP_SMO L2 level adjustments:
op_smo_lib = [
XXX
XXX
]
op_smo_dic = {
XXX : XXX
XXX : XXX
}
for zzz in op_smo_lib:
    x.loc[(x[zz]==zzz), b2c]=op_smo_dic[zzz]
    x.loc[(x['Preferred Name']==zzz), b2c]=op_smo_dic[zzz]
# x.to_csv('checkpoint8.csv')


# ** Step 9: # non-Hinshaw TNO case **

# In[34]:

# build up the lib & dic here ######???:
non_tno_lib_l1 = [
XXX
XXX
] # <-- L1 leaders
non_tno_lib_l2 = [
XXX
XXX
]
non_tno_dic_l1 = {
XXX : XXX
XXX : XXX
}
for zzz in non_tno_lib_l1:
    x.loc[(x[z]!='Hinshaw, John') & (x[l1]=='Technology and Operations') & (x[z]==zzz), b1c]=non_tno_dic_l1[zzz]
for zzz in non_tno_lib_l2:
    x.loc[(x[z]!='Hinshaw, John') & (x[l1]=='Technology and Operations') & (x[zz]==zzz), b2c]=non_tno_dic_l2[zzz]
    
# x.to_csv('checkpoint9.csv')


# ** Step 10: # CSO Quality manually adjustments **

# In[35]:

ql_lib = [
XXX
XXX
]
ql_dic_l1 = {
XXX : XXX
XXX : XXX
}
ql_dic_l2 = {
XXX : XXX
XXX : XXX
}
for zzz in ql_lib:
    x.loc[(x['Business Lvl 3 (Org Chart) Desc']=='HP Quality Office') & (x['Preferred Name']==zzz), b1c]=ql_dic_l1[zzz]
    x.loc[(x['Business Lvl 3 (Org Chart) Desc']=='HP Quality Office') & (x['Preferred Name']==zzz), b2c]=ql_dic_l2[zzz]
    
x.to_csv('Q3_checkpoint10_hpe.csv')


# ** Step n: # Pivot tables for L1/L2 **

# In[36]:

pl1 = pd.pivot_table(x, index=p_index, values=p_values, columns=p_columns1, aggfunc={'Primary Compensation Basis - Amount + PTB Rate (USD)':np.sum, 'Worker ID':len}).loc[mgt_lvl, :]
pl2 = pd.pivot_table(x, index=p_index, values=p_values, columns=p_columns2, aggfunc={'Primary Compensation Basis - Amount + PTB Rate (USD)':np.sum, 'Worker ID':len}).loc[mgt_lvl, :]
# pl1
# pl2


# ** Step n+1: # Export tables to Local **

# In[37]:

pl1.to_csv('OrgLvl1_Q3_hpe.csv', sep=',')
pl2.to_csv('OrgLvl2_Q3_hpe.csv', sep=',')


# In[38]:

'''
mgt = ['EVP', 'SVP', 'VP', 'SFL', 'DIR', 'FEL', 'STR', 'MG2']
pl1.loc[mgt, : ]
'''


# ** Step n+2: # Administration Summary **

# In[39]:

rd = x.copy()
admin = rd[(rd['Job Family Group']=='Administration') & (rd['Job Family']=='Assistants') & (rd['Job Title'].str.contains('Assistant'))]
hpfs_admin = rd[(rd['Job Family Group']=='Administration') & (rd[b2c]=='HFS')& (rd['Job Family']=='Assistants') & (rd['Job Title'].str.contains('Assistant'))]
pad1_Q3 = pd.pivot_table(admin, index=None, values=p_values, columns=p_columns1, aggfunc={'Primary Compensation Basis - Amount + PTB Rate (USD)':np.sum, 'Worker ID':len})
pad2_hpfs_Q3 = pd.pivot_table(hpfs_admin, index=None, values=p_values, columns=p_columns2, aggfunc={'Primary Compensation Basis - Amount + PTB Rate (USD)':np.sum, 'Worker ID':len})
pad1_Q3.to_csv('admin_lvl1_Q3_hpe.csv', sep=',')
pad2_hpfs_Q3.to_csv('admin_hpfs_Q3_hpe.csv', sep=',')


# ** Step n+3: # CSOF break down summary **

# In[40]:

csof =rd[rd[b1c]=='CSOF']
pcs3_Q3 = pd.pivot_table(csof, index=p_index, values=p_values, columns=l3, aggfunc={'Primary Compensation Basis - Amount + PTB Rate (USD)':np.sum, 'Worker ID':len}).loc[mgt_lvl,:]
pcs3_Q3.to_csv('pcs3_Q3_hpe.csv',sep=',')


# **Step n+4: # CTO/Labs NFV split **

# In[41]:

cto = rd[rd[b1c]=='LAB']
nfv = 'Network Functions Virtualization'
l4 = 'Business Lvl 4 (MRU) Desc'
cto_nfv = cto[cto[l4]==nfv]
non_nfv = cto[cto[l4]!=nfv]
nfv_Q3 = pd.pivot_table(cto_nfv, index=p_index, values=p_values, columns=l4, aggfunc={'Primary Compensation Basis - Amount + PTB Rate (USD)':np.sum, 'Worker ID':len}).loc[mgt_lvl,:]
non_nfv_Q3 = pd.pivot_table(non_nfv, index=p_index, values=p_values, columns=p_columns2, aggfunc={'Primary Compensation Basis - Amount + PTB Rate (USD)':np.sum, 'Worker ID':len}).loc[mgt_lvl,:]
nfv_Q3.to_csv('nfv_Q3_hpe.csv',sep=',')
non_nfv_Q3.to_csv('non_nfv_Q3_hpe.csv',sep=',')


# ** Step n+5: # FIN L3 break-down (Corp Dev, IR & Treasury)**

# In[42]:

corpDev = rd[(rd[b1c]=='FIN') & (rd[b2c]=='CDV') & (rd['Business Lvl 3 (Org Chart) Desc']=='Corp Development')]
corpDev_Q3 = pd.pivot_table(corpDev, index=p_index, values=p_values, columns=l3, aggfunc={'Primary Compensation Basis - Amount + PTB Rate (USD)':np.sum, 'Worker ID':len}).loc[mgt_lvl,:]
corpDev_Q3.to_csv('corpDev_Q3_hpe.csv')

