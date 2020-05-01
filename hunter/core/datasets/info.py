import numpy  as np 
import pandas as pd 

# frame-wise
get_info                 = lambda df: df.info()
get_stats                = lambda df: df.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))
get_uniques              = lambda df: df.nunique(axis=0)
get_na                   = lambda df: df.isna().sum()

# columnar-wise
get_col_duplicated       = lambda xs: xs.duplicated().any()
get_col_num_duplicated   = lambda xs: xs.duplicated().shape[0]
get_col_uniques          = lambda xs: xs.unique()


def describe(df):
     print(f"DataFrame Shape: {df.shape}")
     print(f"Columns: {df.columns}")




