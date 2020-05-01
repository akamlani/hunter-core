import numpy as np 

import os 
import glob 
import json 


find_filenames       = lambda path:       glob.glob(path)                   # find_filenames('data/names/*.txt')
get_filename         = lambda path:       os.path.basename(path)            # filename      = get_filename('data/names/French.txt') => French.txt
split_file_extension = lambda filename:   os.path.spittext(filename)        # filename, ext = split_file_extension(French.txt')     => French, txt

numpy_load_text_file = lambda filename:   np.loadtxt(filename, dtype=str)   # load textfile into numpy array



def load_text(path:str) -> str:
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


def load_lines(path, delimiter='\n'):
    """Load a series of lines from a text file from the provided url.
    
    Args:
        path (str): url of string to load and decode
        delimiter (str, optional): delimiter to split on

    Returns:
        str: text
    """
    dat = load_text(path).split(delimiter)
    return dat


def convert_dict_to_json(data_dict:dict) -> str:
    """convert a dictionary to json string"""
    return json.dumps(data_dict, indent=4, sort_keys=True)

def write_json(data_dict:dict, filename:str='object.json'):
    """write dictionary as a json string to file"""
    with open(filename, 'w') as f:
        json.dump(data_dict, f)
        
def read_json(filename:str) -> str:
    """read a json string from a file"""
    with open(filename, 'r') as f:
        data = json.load(f)
    return data