#!/bin/bash

base1="ali"
base2="beast"
base3="four"

# VR1="iaiaila"
# VR2="asteb"
VR1=$1
VR2=$2

NB1=$(echo $VR1 | tr $base1 "012")
NB2=$(echo $VR2 | tr $base2 "01234")

NB1_10=$(echo "ibase=3; $NB1" | bc)
NB2_10=$(echo "ibase=5; $NB2" | bc)

NB_FINAL=$(echo $(($NB2_10 + $NB1_10)))
echo "obase=4; ibase=10; $NB_FINAL" | bc | tr "0123" 'four'
