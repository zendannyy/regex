#!/usr/bin/env bash
# shebang is for UNix systems, so users PATH is respected

set -e
_B='\033[1m'
_R='\033[0;31m'
_G='\033[0;32m'
_Z='\033[0m'

# RegEx 3 and 4 are different variations for IP addresses
regex3="^[0-9\.]{7,15}$"
octet="([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
regex4="^$octet\.$octet\.$octet\.$octet$"

if [ -z $1 ]; then
    echo Usage: $0 \<string to match\>
    exit
fi
echo -ne ${_Z}
echo Trying to match [$1]

# validators
[[ $1 =~ $regex3 ]] && \
    echo -e \* [${_B}$1${_Z}] ${_G}matches regexp${_Z}: $regex3 || \
    echo -e \* [${_B}$1${_Z}] ${_R}DOES NOT MATCH${_Z}: $regex3

[[ $1 =~ $regex4 ]] && \
    echo -e \* [${_B}$1${_Z}] ${_G}matches regexp${_Z}: $regex4 || \
    echo -e \* [${_B}$1${_Z}] ${_R}DOES NOT MATCH${_Z}: $regex4

