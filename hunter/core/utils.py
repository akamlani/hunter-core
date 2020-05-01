from __future__ import print_function, absolute_import, division

import  warnings                                                        #warnings.filterwarnings("ignore") 

from    collections.abc import ABC, Mapping, abstractmethod             # collections.abc (Abstract Base Classes)
from    array import array                                              # restrict by typecode
from    typing import Iterable, List

from    tqdm import tqdm                                                #tqdm.pandas(), .progress_apply

import  numpy as np 
import  scipy.sparse as sp                                              # sp.csr_matrix

exists_attr           = lambda x, attr:     hasattr(x, attr)
get_class_name_type   = lambda inst:        type(inst).__name__
get_class_name_inst   = lambda inst:        inst.__class__.__name__
get_name              = lambda fn:          fn.__name__
get_module            = lambda fn:          fn.__module__


check_instance        = lambda X, tp:       isinstance(X, tp)           # checks if an appropriate type: check_instance(X, Mapping)
convert_dtype         = lambda v:           np.float64(v)








