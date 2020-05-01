import numpy  as np 
import pandas as pd 

def standardize_col_names(df):
    """lowercase column names of a dataframe

    Args:
        df (dataframe): pandas dataframe

    Returns:
        df: tranformed dataframe
    """    
    df.columns = df.columns.map(lambda col: col.lower())
    return df 


def one_hot_encode(arr, num_labels):
    """Perform Aggregation to build a list of sequence per group and perform sorted count aggregations

    Args:
        array (numpy): numpy array
        num_labels (i): number of labels or categories

    Returns:
        one_hot: numpy array OHE
    """    
    # Initialize the the encoded array
    one_hot = np.zeros((arr.size, num_labels), dtype=np.float32)
    # Fill the appropriate elements with ones
    one_hot[np.arange(one_hot.shape[0]), arr.flatten()] = 1.
    # Finally reshape it to get back to the original array
    one_hot = one_hot.reshape((*arr.shape, num_labels))
    return one_hot

def create_sequences(df, grouping_cols:list, aggregation_col:str):
    """Perform Aggregation to build a list of sequence per group and perform sorted count aggregations

    Args:
        df (dataframe): pandas dataframe
        grouping_cols (list): list of string column names to group on
        aggregation_cols (str): aggreation column to perform collection on per group

    Returns:
        df: tranformed dataframe
    """    
    aggr_seq_col = f"{aggregation_col}_sequence"
    df_agg = pd.DataFrame(df.groupby(grouping_cols)[aggregation_col].apply(lambda x: x.tolist()))
    df_agg = df_agg.rename(columns={aggregation_col: aggr_seq_col}).reset_index()
    df_agg[f"{aggr_seq_col}_counts"]        = df_agg[aggr_seq_col].apply(lambda x: len(x))
    df_agg[f"{aggr_seq_col}_unique_counts"] = df_agg[aggr_seq_col].apply(lambda x: len(np.unique(x))) 
    df_agg = df_agg.sort_values(by=f"{aggr_seq_col}_counts", ascending=False)
    return df_agg
