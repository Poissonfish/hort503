#!/bin/bash
SRAs=$(cat SRA_IDs.txt)
for SRA in $SRAs
do
	if [ ! -d $SRA ]
	then
		mkdir $SRA
	fi
done
