#!/bin/bash

ZAHL=$(cat kant.txt | tr '",.;:)\r' ' ' | tr -s ' ' '\n' | sort | \
uniq -c -i -d | sort -rn | grep -n "Vernunft" | head -1l | cut -d: -f1)
echo "Das Wort 'Vernunft' ist an der Stelle" $ZAHL "der häufigsten Wörter"
