import shutil 
import os 
import glob 
import json 
import pickle 

from pathlib import Path


copy_to_dest = lambda src_dir, dst_dir: shutil.copy(src_dir, dst_dir)

def write_creds(path, creds:dict):
    """ write credentials to a file

    Arguments:
        path (str): path to where json credentials file is located
        creds (dict): dictionary of username, password credentials
    
    Example:
        >>> path  = '~/.kaggle/kaggle.json'
        >>> creds = '{"username":"xxx","key":"xxx"}'
        >>> write_creds(path, creds)
    """
    creds     = json.dumps(creds) 
    cred_path = Path('~/.kaggle/kaggle.json').expanduser()
    if not cred_path.exists():
        cred_path.parent.mkdir(exist_ok=True)
        cred_path.write(creds)
        cred_path.chmod(0o600)

def write_pickle(data, file_path):
    """write binary contents to a pickle file"""
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

def write_json(data_dict:dict, file_path:str='object.json') -> None:
    """dump contents to a file via json"""
    with open(file_path, 'w') as f:
        json.dump(data_dict, f, indent=4)

