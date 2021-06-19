#!/bin/bash

if [[ $# -eq 0 ]]
then
    echo 'Path to data file is expected as an argument.'
    exit 0
elif [[ $# -gt 1 ]]
then
    echo 'Too many arguments were passed. Expected: 1.'
else
    python count_islands.py $1
fi