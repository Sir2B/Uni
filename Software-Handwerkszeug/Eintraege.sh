#!/bin/bash
SUMME=0
for i in $(ls /home); do
	#echo $i
	#ls /home/$i | wc -w
	SUMME=$(($SUMME + $(ls /home/$i | wc -w)))
done
echo $SUMME

#for d in $(ls /home/) ; do   echo $d $(ls $d | wc -w); done | awk '{s += $2} END
