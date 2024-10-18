#!/bin/bash
#
#SBATCH --job-name=test_trainer_noGPU
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=10:30:00
#SBATCH --partition=earth-1
#SBATCH --constraint=rhel8


# Load the Anaconda module (adjust to the available version on your cluster)
module load gcc/7.3.0 miniconda3/4.8.2 lsfm-init-miniconda/1.0.0
# module load gcc/9.4.0-pe5.34 miniconda3/4.12.0 lsfm-init-miniconda/1.0.0
# module load cuda/11.6.2

# Activate your Conda environment
source activate tinysleepnet_env

# Run your Python script
python trainer.py --db sleepedf --gpu -1 --from_fold 0 --to_fold 19

conda deactivate
