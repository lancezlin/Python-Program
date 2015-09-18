import pandas as pd
def get_sal_col(df):
    salary_col = []
    for col in list(df.columns.values):
        if "PTB" in col:
            salary_col.append(col) # get all column names contains PTB rate
        else:
            continue
    return salary_col
