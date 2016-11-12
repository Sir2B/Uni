#!/bin/bash

ZAHL=$(cat genom.txt | grep 'CGATTG' | wc -w)
echo "Anzahl: " $ZAHL
