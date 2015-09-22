import pandas as pd
def col_cont_str(df, string): # df is data frame, string is a key word or sub key word
    _col = []
    for col in list(df.columns.values):
        if string in col:
            _col.append(col) # e.g. get all column names contains PTB rate
        else:
            continue
    return _col
