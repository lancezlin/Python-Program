import pandas as pd
import numpy as np
import os
%cd "C:\Users\linla\Documents\Assignments\R_SAS_Data"
##
def bridgeAnalysis(org, pre, cur):
    wid = 'Worker ID'
    orgL1 = 'Business Lvl 1 (Group) Code'
    mgt = 'Management Level'
    mg2_ab = ['EVP', 'SVP', 'VP', 'SFL', 'DIR', 'FEL', 'STR', 'MG2']
    fieldRetain1 = ['Report Date', 'Worker ID', 'Preferred Name', 'Management Level','Business Lvl 1 (Group) Code','Movements','Management Level','Business Lvl 1 (Group) Code']
    fieldRetain2 = ['Report Date_x', 'Worker ID', 'Preferred Name_x', 'Management Level_x','Business Lvl 1 (Group) Code_x','Movements', 'Management Level_y','Business Lvl 1 (Group) Code_y']
    # Subset dataset to narrow down by each L1 leader
    org_pre = pre[(pre[mgt].isin(mg2_ab)) & (pre[orgL1]==org)]
    org_cur = cur[(cur[mgt].isin(mg2_ab)) & (cur[orgL1]==org)]
    
    # Voluntary or Involuntary exits:
    svv_pre = pd.merge(org_pre, cur, how='inner', on=wid, copy=False)
    terms = org_pre[~org_pre[wid].isin(svv_pre[wid])]  # should break down to voluntary and involuntary
    if len(terms)>0:
        terms.loc[:, 'Movements']='Exit/Active to Inactive'
        exExit = terms.loc[:,fieldRetain1]
        exExit.columns=fieldRetain2
    else:
        exExit = pd.DataFrame()
        
    # internal exits:
    internal_exits = svv_pre[~svv_pre[wid].isin(org_cur[wid])]  # should break down to demotions and transfer out
    if len(internal_exits)>0:
        internal_exits.loc[(internal_exits['Business Lvl 1 (Group) Code_y']!=org),'Movements']='Transfer Out'
        internal_exits.loc[(internal_exits['Business Lvl 1 (Group) Code_y']==org) & (~internal_exits['Management Level_y'].isin(mg2_ab)),'Movements']='Demotion'
        interExit = internal_exits.loc[:,fieldRetain2]
        interExit.columns=fieldRetain2
    else:
       interExit = pd.DataFrame()
    
    # external adds:
    svv_cur = pd.merge(org_cur, pre, how='inner', on=wid, copy=False)
    ex_adds = org_cur.loc[~org_cur[wid].isin(svv_cur[wid])]
    if len(ex_adds)>0:
        ex_adds.loc[:,'Movements']='Adds/Inactive to Active'
        exAdd = ex_adds.loc[:,fieldRetain1]
        exAdd.columns=fieldRetain2
    else:
        exAdd = pd.DataFrame()
    # internal adds
    internal_adds = svv_cur[~svv_cur[wid].isin(org_pre[wid])]   # should break down to premotion and transfer in
    if len(internal_adds)>0:
        internal_adds.loc[(internal_adds['Business Lvl 1 (Group) Code_y']!=org),'Movements']='Transfer In'
        internal_adds.loc[((internal_adds['Business Lvl 1 (Group) Code_y']==org) & (~internal_adds['Management Level_y'].isin(mg2_ab))),'Movements']='Promotion'
        interAdd = internal_adds.loc[:,fieldRetain2]
        interAdd.columns=fieldRetain2
    else:
        interAdd = pd.DataFrame()
    mvtSummary = exExit.append([interExit, exAdd, interAdd])
    # print exExit, interExit, exAdd, interAdd
    #print org_pre.iloc[:,[8,9]]
    #print svv_pre.iloc[:,[8,9]]
    return mvtSummary
