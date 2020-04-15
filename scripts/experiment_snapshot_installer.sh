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
EXPERIMENTS_HOME=${UNIX_HOME}/dev-platform/experiments

# Specific Snapshot Experiment Structure 
SNAPSHOTS_HOME=${EXPERIMENTS_HOME}/snapshots
TEMPLATE_HOME=${SNAPSHOTS_HOME}/${TEMPLATE_NAME}
mkdir -p ${TEMPLATE_HOME}/man
mkdir -p ${TEMPLATE_HOME}/env
mkdir -p ${TEMPLATE_HOME}/releases

mkdir -p ${TEMPLATE_HOME}/external/tools
mkdir -p ${TEMPLATE_HOME}/external/jars/{packages,scripts}

mkdir -p ${TEMPLATE_HOME}/scripts
mkdir -p ${TEMPLATE_HOME}/tests
mkdir -p ${TEMPLATE_HOME}/apps/{nbs,programs}

mkdir -p ${TEMPLATE_HOME}/data/{conf,sources}
mkdir -p ${TEMPLATE_HOME}/exports/{data,artifacts,ckpts,figures,logs,metrics,reports}
echo "UNIX Experiment Snapshot '${TEMPLATE_NAME}' Structure Installed"
