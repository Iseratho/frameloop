#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gpus-per-node=1

# Change to local storage on assigned node
# cd ~/local

# And run the program
python -m pip install framefinder sentence_transformers penman matplotlib seaborn
python mindframes.py