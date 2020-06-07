import  numpy as np 
import  os 
import  glob 
import  json 

import  joblib 
from    pathlib import Path


find_filenames       = lambda path:       glob.glob(path)                   # find_filenames('data/names/*.txt')
get_filename         = lambda path:       os.path.basename(path)            # filename      = get_filename('data/names/French.txt') => French.txt
split_file_extension = lambda filename:   os.path.spittext(filename)        # filename, ext = split_file_extension(French.txt')     => French, txt

numpy_load_text_file = lambda filename:   np.loadtxt(filename, dtype=str)   # load textfile into numpy array
expand_user_home     = lambda s:          Path(s).expanduser()              # Path('~/.kaggle/kaggle.json').expanduser()
                                                                                              

#useful for loading a pickle file 
load_artifact        = lambda artifact_path: joblib.load(artifact_path)


def read_pickle(path:str) -> dict:
    "extract pickle data into a dictionary"
    import pickle
    with open(path, 'rb') as f:
        data_dict = pickle.load(f, encoding='bytes')
    return data_dict
        
def read_pkl_gzip(path:str) -> tuple:
    "exactracle pickle gzip data"
    import gzip 
    import pickle
    with gzip.open(path, 'rb') as f:
        train_set, valid_set, test_set = pickle.load(f, encoding='iso-8859-1')
    return train_set, valid_set, test_set
        

def read_text(path:str) -> str:
    """Load a text file from the provided url.
    
    Args:
        path (str): url of string to load and decode

    Returns:
        str: text
    """
    with open(path, 'r', encoding='UTF-8') as f:
        text = f.read()
        text.strip()
    return text


def read_lines(path, delimiter='\n'):
    """Load a series of lines from a text file from the provided url.
    
    Args:
        path (str): url of string to load and decode
        delimiter (str, optional): delimiter to split on

    Returns:
        str: text
    """
    dat = read_text(path).split(delimiter)
    return dat
        
def read_json(filename:str) -> str:
    """read a json string from a file"""
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def convert_dict_to_json(data_dict:dict) -> str:
    """convert a dictionary to json string"""
    return json.dumps(data_dict, indent=4, sort_keys=True)
