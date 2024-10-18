#!/bin/bash
#
#SBATCH --job-name=cnn-tf-gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:30:00
#SBATCH --partition=earth-4
#SBATCH --constraint=rhel8
#SBATCH --gres=gpu:l40s:1


# Load the Anaconda module (adjust to the available version on your cluster)
module load gcc/9.4.0-pe5.34 miniconda3/4.12.0 lsfm-init-miniconda/1.0.0
module load cuda/11.6.2 


# Activate your Conda environment
source activate tinysleepnet_env4

# Run your Python script
python simple_test_model.py
python test_gpu.py

# Deactivate the environment (optional, but good practice)
conda deactivate