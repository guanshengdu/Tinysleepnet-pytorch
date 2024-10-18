#!/bin/bash
#
#SBATCH --job-name=cnn-tf-gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=10:30:00
#SBATCH --partition=earth-4
#SBATCH --constraint=rhel8
#SBATCH --gres=gpu:l40s:1

# Load the Anaconda module (adjust to the available version on your cluster)
module module load gcc/9.4.0-pe5.34 miniconda3/4.12.0 lsfm-init-miniconda/1.0.0

# Activate your Conda environment
source activate tinysleepnet_env2

# Run your Python script
python trainer.py --db sleepedf --gpu 0 --from_fold 0 --to_fold 19

