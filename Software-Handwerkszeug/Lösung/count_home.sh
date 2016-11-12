#!/bin/bash

for I in $(ls /home/); do
    #echo $I
    ls /home/$I/ | wc -l
done
