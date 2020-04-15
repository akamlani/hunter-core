# Hunter-Core
Represents Machine Learning and Deep Learning Core Library functionality

## Installation
Install Experiment Structure
```sh 
# installs experiment structure in $HOME/dev-platform/experiments
./scripts/experiment_snapshot_installer.sh template_name     # create experiment structure
```

Activate Environment
```sh
# update anaconda 
conda update conda 
# create a mck anaconda environment first based on python 3.x 
cd env 
conda env create -f <template>.v3_x.yml       # create python nlp environment package dependencies from existing
conda env list                                # list environments
source activate ml.base.v37                   # select environment (make sure executed anytime python scripts for nlp depdendencies are executed)
                                              # conda create --name deeplearning.core.v37 --clone ml.base.v37
# for spacy nlp specifics
python -m spacy download en                   # download a smaller model 
python -m spacy download en_core_web_md       # download a larger model for a larger vocabulary
```

Install Libraries and Dependencies 
```sh
# installs the library in 'edit' mode for development into prior installed environment
# show be installed as: `hunter-workflows` in listing the packages (conda list |less )
cd hunter-core
pip install -e .  
```

## Create Symoblic Links
Create symbolic links to execute within Experiment Structure if applicable

```sh
cd $HOME/experiments/snapshots/{template_name}
rm -rf apps
ln -s $HOME/Projects/repositories/{template_name}/apps/ apps

rm -rf data/conf
ln -s $HOME/Projects/repositories/{template_name}/resources/data/conf/ data/conf
```

## Citations
------------------
If you reference in your research, please cite:
```
@article{Hunter2020,
    author = {Kamlani, Ari},
    title  = {{Spinning up core Machine Leanring and Deep Learning Frameworks}},
    year   = {2020}
}
```