#!/bin/sh 

port_id=7870
ssh -N -f -L localhost:${port_id}:localhost:${port_id} ${USER}@${CLUSTER_HOME}
