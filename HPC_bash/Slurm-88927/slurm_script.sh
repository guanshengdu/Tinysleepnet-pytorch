#!/bin/bash
#
#SBATCH --job-name=HPC_bash2
#SBATCH --nodes=1
#SBATCH --ntasks=24
#SBATCH --time=1:00:00
#SBATCH --partition=earth-1
#SBATCH --mem=32G
#SBATCH --constraint=rhel8

# Load the Anaconda module (adjust to the available version on your cluster)
module module load gcc/9.4.0-pe5.34 miniconda3/4.12.0 lsfm-init-miniconda/1.0.0

# Activate your Conda environment
source activate tinysleepnet_env2

# Run your Python script
python test.py

