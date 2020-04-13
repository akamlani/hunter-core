# Machine Learning / Deep Learning Workflows and Experiment Structure

## Scripts
- **cluster_dbg.sh**: for remotely debugging across a cluster (SPARK Centric)
- **experiment_root_installer.sh**: root structure installer
- **experiment_snapshot_installer.sh**: snapshot template for an experiment 
- **libs_structure_installer.sh**: install the library structure

## Install Experiment Structure
```sh 
# installs experiment structure in $HOME/experiments
./scripts/experiment_root_installer.sh                       # create experiment structure
./scripts/experiment_snapshot_installer.sh template_name     # create experiment structure
./scripts/libs_structure_installer.sh asr                    # create library structure
```

## Install Python Environment
Install [Anaconda Python 3](https://www.anaconda.com/distribution/#download-section)

```sh
# update anaconda 
conda update conda 
# create a mck anaconda environment first based on python 3.x 
cd env 
conda env create -f <template>.v3_x.yml       # create python nlp environment package dependencies from existing
conda env list                                # list environments
source activate exxonmobile.asr.v37           # select environment (make sure executed anytime python scripts for nlp depdendencies are executed)
python -m spacy download en                   # download a smaller model 
python -m spacy download en_core_web_md       # download a larger model for a larger vocabulary
```

## Install Demand Forecast Specific Library 

```sh
# installs the library in 'edit' mode for development into prior installed environment
# show be installed as: `hunter-workflows` in listing the packages (conda list |less )
cd hunter
pip install -e .  
```

## Create Symoblic Links
Create symbolic links to execute within Experiment Structure 

```sh
cd $HOME/experiments/snapshots/{template_name}
rm -rf apps
ln -s $HOME/Projects/repositories/{template_name}/apps/ apps

rm -rf data/conf
ln -s $HOME/Projects/repositories/{template_name}/resources/data/conf/ data/conf
```

Citations
------------------
If you reference in your research, please cite:
```
@article{Hunter2020,
    author = {Kamlani, Ari},
    title  = {{Spinning up Deep Learning Frameworks}},
    year   = {2020}
}
```