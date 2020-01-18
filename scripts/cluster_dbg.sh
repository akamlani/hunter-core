#!/bin/sh

OPTIND=1  #for sourcing a script

DEFAULT_DEBUG_STATE='n'
DEFAULT_DEBUG_PORT=5005

function usage { 
  echo "Usage for $(basename $0):"
  echo "$(basename $0) -h           enables help usage menu"
  echo "$(basename $0) -c <port>    check if port is already listening"
  echo "$(basename $0) -p <port>    default port=5005"
  echo "$(basename $0) -d           enables remote debugging0"
  echo "$(basename $0) -d -p 9000   enables remote debugging, configure remote debug as port 9000"
  echo "$(basename $0)              disables remote debugging"
}

# configure initial default states
suspend_state=${DEFAULT_DEBUG_STATE}
port=${DEFAULT_DEBUG_PORT}


while getopts "hdp:c:" opt; do
    case ${opt} in
      h)
        usage
        exit;;
      p)
        port=${OPTARG}
        echo "Set Port for Remote Debugging: ${port}"
        ;;
      c)
        port=${OPTARG}
        echo "Checking if Port is already Listening:"
        #netstat -a |grep LISTEN
        lsof -i:${port}
        exit
        ;;
      d)
        suspend_state='y'
        echo "Enable Remote Debugging Service: ${suspend_state}"
        ;;
      ?)
        echo "Unknown Command Option, See Usage..."
        usage
        exit;;
    esac 
done

# handles case for no options to disable remote debugging
if [ $OPTIND -eq 1 ]; then 
  echo "Disabling remote debugging service...";
else
  echo "Configuring Remote Debug Service..."
fi

# note this script needs to be adapted for teh proper environment
export SPARK_SUBMIT_OPTS=-agentlib:jdwp=transport=dt_socket,server=y,suspend=${suspend_state},address=${port}
echo   ${SPARK_SUBMIT_OPTS}
shift  $((OPTIND-1))

echo "Ending Configuration Service..."
