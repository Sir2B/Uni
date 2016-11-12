#!/bin/bash

cat kant.txt | tr '",.;' ' ' | tr -s ' ' '\n' | grep Vernunft | sort | uniq -c | sort -rn 
