#!/bin/sh
LIBS_PACKAGE=$1

usage()  
{  
    echo "ERROR => Usage: $0 libname"  
    exit 1  
} 

if [ $# -ne 1 ] ; then usage; fi

# UNIX Structure
UNIX_HOME=${HOME}
EXPERIMENTS_HOME=${UNIX_HOME}/experiments
# Library Structure
LIBS_HOME=${EXPERIMENTS_HOME}/libs
LIBS_NAME=${LIBS_HOME}/${LIBS_PACKAGE}/${LIBS_PACKAGE}

mkdir -p ${LIBS_NAME}/apps/{nbs,programs,tests}
mkdir -p ${LIBS_NAME}/{utils,ml}
echo "UNIX Library '${LIBS_PACKAGE}' Structure Installed"
echo "UNIX Library '${LIBS_NAME}' Path Structure Installed"
