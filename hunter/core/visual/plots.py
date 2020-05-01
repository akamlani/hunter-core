import numpy as np

import matplotlib.pyplot as plt 
import seaborn as sns 


def set_axis_opts(axi, **kwargs):
    "axis configuration for visualization plotting"
    params   = {
        'fontweight':'regular', 
        'fontstyle':'italic', 
        'fontsize':  kwargs.get("fontsize", 14)
    }
    fn_dict = lambda axi: {
        "title":        axi.set_title,
        "xaxis-label":  axi.set_xlabel,
        "yaxis-label":  axi.set_ylabel,
        "legend-title": axi.legend
    }
    kw_dict = {k:v for k,v in kwargs.items() if k not in params}
    for k,v in kw_dict.items():
        fn_dict(axi)[k](v, **params)   
    return axi