import numpy as np 
import pandas as pd 
import random as rn

shuffle_data = lambda data: rn.shuffle(data)

def describe_partition(inp_tensor_train, inp_tensor_val, tgt_tensor_train, tgt_tensor_val):
    """describe partition sizes"""
    cols  = ["Inp-Train", "Tgt-Train", "Inp-Validation", "Tgt-Validation"]
    sizes = [len(inp_tensor_train), len(tgt_tensor_train), len(inp_tensor_val), len(tgt_tensor_val)]
    df_partition = pd.DataFrame(sizes, index=cols).rename(columns={0:'size'}).T
    return df_partition

def shuffle_partition(X, y):
    """shuffle partition based on random shuffle of indices
    
    Args:
        X (numpy array or list): features
        y (numpy array or list): target data    
    """
    indices = np.arange(len(X))
    np.random.shuffle(indices)
    return X[indices], y[indices]


def partition_data(df, testing_split=0.3, shuffle=True):
    """partition and shuffle a given dataset
    
    Args:
        df (dataframe): pandas dataframe to partition
        testing_split (float): testing partition fraction size
        shuffle (boolean): determines to shuffle the dataset or not

    """
    dataset_size   = len(df)
    training_split = 1 - testing_split 

    training_length = int(dataset_size * training_split)
    testing_length  = int(dataset_size - training_length)
    df_shuffled     = shuffle_data(df.sample(n=dataset_size))
    training_set    = df_shuffled[0:training_length]
    testing_set     = df_shuffled[:testing_length]
    return training_set, testing_set

def create_random_samples(num_items, shape, random_state=None):
    """create a set of random samples

    Args:
        num_items (int): total number of items from which we should sample
        shape(int or tuple): shape of sampled array 
        random_state (np.random.RandomState, optional): random state to use for sampling.

    Returns:
        items (numpy array): np.array of shape [shape] sampled item ids
    """
    if random_state is None:
            random_state = np.random.RandomState()

    items = random_state.randint(0, num_items, shape, dtype=np.int64)
    return items
