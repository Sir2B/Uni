#!/bin/bash
#
########################################################
# some Slurm directives
#
# Job name in Slurm
#SBATCH -J PrimeSuche
# limit for CPU time (8h)
#SBATCH --time=08:00:00
########################################################
#
# find primes from $plow to $plow + $nrange 
plow=3
nrange=15000000
python findprimes.py $plow $nrange
