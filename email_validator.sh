#!/usr/bin/env bash
# shebang is for Unix systems, so users PATH is respected

set -e
_B='\033[1m'
_R='\033[0;31m'
_G='\033[0;32m'
_Z='\033[0m'

# These RegExes are designed for an email address
regex1="^[a-zA-Z0-9\+\-\._]+@[a-zA-Z0-9\.\-]+$"
regex2="^[[:alnum:]\+\-\._]+@[[:alnum:]\.\-]+$"


if [ -z $1 ]; then
    echo Usage: $0 \<string to match\>
    exit
fi
echo -ne ${_Z}
echo Trying to match [$1]

# validators
[[ $1 =~ $regex1 ]] && \
    echo -e \* [${_B}$1${_Z}] ${_G}matches regexp${_Z}: $regex1 || \
    echo -e \* [${_B}$1${_Z}] ${_R}DOES NOT MATCH${_Z}: $regex1

[[ $1 =~ $regex2 ]] && \
    echo -e \* [${_B}$1${_Z}] ${_G}matches regexp${_Z}: $regex2 || \
    echo -e \* [${_B}$1${_Z}] ${_R}DOES NOT MATCH${_Z}: $regex2
