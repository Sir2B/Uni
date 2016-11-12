#!/bin/bash
SUMME=0
for i in $(ls /home); do

	SUMME=$(($SUMME + $(ls /home/$i | grep 'Markus' | wc -w)))
done
echo $SUMME
# ls /home/m | grep 'Markus' | wc -w
