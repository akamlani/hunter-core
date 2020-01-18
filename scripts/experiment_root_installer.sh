#!/bin/sh

### UNIX Structure
UNIX_HOME=${HOME}
EXPERIMENTS_HOME=${UNIX_HOME}/experiments
# Common Structure
mkdir -p ${EXPERIMENTS_HOME}/env                            # environment exports
mkdir -p ${EXPERIMENTS_HOME}/man                            # global documents, manuals
mkdir -p ${EXPERIMENTS_HOME}/libs                           # libraries for installation
mkdir -p ${EXPERIMENTS_HOME}/scripts                        # global scripts
mkdir -p ${EXPERIMENTS_HOME}/tools                          # global tools
mkdir -p ${EXPERIMENTS_HOME}/templates/conf                 # templates (e.g. experiment conf files)
mkdir -p ${EXPERIMENTS_HOME}/jars/{packages,apps,scripts}
mkdir -p ${EXPERIMENTS_HOME}/data/{share,man,releases,sources,exports}
echo "UNIX Experiment Common Root Structure Installed"
