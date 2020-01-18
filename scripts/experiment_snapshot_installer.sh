#!/bin/sh
TEMPLATE_NAME="template_name"

usage()  
{  
    echo "ERROR => Usage: $0 templatename"  
    echo "Using Default Structure: ${TEMPLATE_NAME}"
} 

if [ $# -ne 1 ] ; 
    then usage; 
else 
    TEMPLATE_NAME=$1
fi

### UNIX Structure
UNIX_HOME=${HOME}
EXPERIMENTS_HOME=${UNIX_HOME}/experiments

# Specific Snapshot Experiment Structure 
SNAPSHOTS_HOME=${EXPERIMENTS_HOME}/snapshots
TEMPLATE_HOME=${SNAPSHOTS_HOME}/${TEMPLATE_NAME}
mkdir -p ${TEMPLATE_HOME}/man
mkdir -p ${TEMPLATE_HOME}/apps/{nbs,programs,tests}
mkdir -p ${TEMPLATE_HOME}/jars/{packages,apps,scripts}
mkdir -p ${TEMPLATE_HOME}/data/{conf,sources}
mkdir -p ${TEMPLATE_HOME}/exports/{artifacts,ckpts,data,figures,logs,metrics,reports}
echo "UNIX Experiment Snapshot '${TEMPLATE_NAME}' Structure Installed"
