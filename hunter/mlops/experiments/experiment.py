import numpy as np 

import os 
import time
import shutil 
import logging 


logger = logging.getLogger(__name__)

class Experiment(object):
    """Create experiment directory structure, track, and store data.

    To be used as a base class or derived `Experiment` classes.    
    """


    def __init__(self, project_name:str, experiment_dir:str="dev-platform/experiments/snapshots", tags:list=None) -> None:
        """Initialize Experiment class instance.

        Args:
            project_name (str): Name of Project
            experiment_dir (str, optional): Path of location to experiment snapshots
            param3 (:obj:`list` of :obj:`str`): List of Tags to associate with experiment

        """
        super().__init__()
        # copy directory structure to project name 
        user_home         = os.getenv("HOME")
        experiment_dir    = os.path.join(user_home,      experiment_dir)
        template_dir      = os.path.join(experiment_dir, "template")
        project_dir       = os.path.join(experiment_dir,  project_name)


        self._project_dir = project_dir
        self._export_dir  = os.path.join(self._project_dir, "exports")
        self._model_dir   = os.path.join(self._export_dir,  "artifacts")
        self._copy_dir_template(template_dir, project_dir)

        self._tags        = {k: v for k,v in tags.items()}
        self._name        = project_name 
        self._id          = -1

    def list_project_dir(self):
        print( os.listdir(self._project_dir) )

    @property
    def name(self):
        return self._name

    @property
    def experiment_id(self):
        return self._id

    @property
    def tags(self):
        return self._tags

    def add_data_uri(self, data_uri):
        self.datasrc_uri = data_uri

    def add_vocab_uri(self, vocab_uri):
        self.vocabsrc_uri = vocab_uri

    def _add_tag(self, tag):
        self._tags[tag.key] = tag.value 

    def _copy_dir_template(self, src, dest):
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(src, dest)

    def __repr__(self):
        return f"{self.name}"

