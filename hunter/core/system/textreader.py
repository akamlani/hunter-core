import numpy as np 
import pandas as pd 
import glob
import os

from functools import reduce

class TextReader(object):
    
    @staticmethod
    def load(root_path, partitions, labels, shuffle=False, num_files=None):
        """discover and load content
        
        Example
            >>> root_path = experiment.datasrc_uri
            >>> Reader.load(root_path, partitions=["train", "test"], labels=["pos", "neg", "unsup"])
        """
        df        = TextReader._search(root_path, partitions, labels, shuffle)            
        num_files = [len(df) if not num_files else num_files]
        df        = df[:num_files[-1]]
        df        = df.apply(TextReader._load_content, axis=1)
        return df
    
    @staticmethod
    def _search(root_path, partitions, labels, shuffle=False):
        contents = []
        for partition in partitions:
            for label in labels:
                path      = os.path.join(partition, label)
                path      = os.path.join(root_path, path)
                files     = glob.glob(path + '/*')
                contents.append( list( zip([partition]*len(files), [label]*len(files), files) ) )
        df = pd.DataFrame(reduce(lambda x,y: x+y, contents), columns=['partition', 'label', 'path'])
        return (df.sample(frac=1.0) if shuffle else df)
    
    @staticmethod
    def _load_content(ds):
        with open(ds.path, 'r') as f:
            ds['text'] = f.read()
        return ds
