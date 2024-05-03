#!/bin/bash
if [[ -x "$(command -v python3)" ]]
then
    source ./run_gallo_24_garage.sh
else
    echo "It appears python is not installed on this device or you have the wrong version. Please install python version 3 or above to use this application." >&2
fi