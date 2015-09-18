# can be used to count the distinct value by row in a data frame #

import pandas as pd

def count_dist_row(df):
    df = df.fillna(0) # make sure NA was cleaned.
    shape_df = shape(df)
    max_row = shape_df[0]
    max_col = shape_df[1]
    count_list = []
    i =0
    while i < max_row:
        j = 0
        blist = []
        while j < max_col:
            if d.iloc[i, j] not in blist:
                blist.append(d.iloc[i,j])
                j += 1
            else:
                j += 1
        count_dict = {'Freq' : len(blist)-1}
        count_list.append(count_dict)
        i += 1
    df_count = pd.DataFrame(count_list)
    df_fnl = pd.merge(df, df_count, right_index = True, left_index = True, how = 'left')
    return df_fnl  # return a dataframe to add back to the old df
