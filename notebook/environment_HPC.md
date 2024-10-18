## 09.10.2024

Read HPC wiki. 

Upload sleep-cassette sleeping data to the data folder.

## Connect to HPC

```bash
ssh dugua001@login-rhel7.hpc.zhaw.ch
```
OR
```bash
ssh dugua001@login-rhel8.hpc.zhaw.ch
```

### Home directory on HPC
```
/net/home/dugua001/
```
### Working directory on HPC
```
/cfs/earth/scratch/dugua001/
```


## Set Git

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

## Load Conda software environment on HPC.

```bash
module load gcc/9.4.0-pe5.34 miniconda3/4.12.0 lsfm-init-miniconda/1.0.0 # Load in USS/2022: 4.12.0 (GCC 9.4.0-pe5.34) 
module load gcc/7.3.0 miniconda3/4.8.2 lsfm-init-miniconda/1.0.0 # USS/2020: 4.8.2 (GCC 7.3.0)
```
## Add '~/.condarc' file to the home directory.

```~/.condarc
# # use conda config --describe <keyword> to get infos
# # e.g. conda config --describe channels

channels:
      - conda-forge
      - defaults

channel_priority: strict

envs_dirs:
    - /cfs/earth/scratch/$USER/.conda/envs

pkgs_dirs:
    - /cfs/earth/scratch/$USER/.conda/pkgs

env_prompt: '({default_env}) '

auto_activate_base: false

```

## Create a Conda environment for Tinysleepnet.

```bash
conda create -n tinysleepnet_env python=3.6
conda install numpy=1.16
conda install pandas=0.24
conda install scikit-learn=0.20
conda install scipy=1.2
conda install matplotlib=3.0
conda install pyEDFlib=0.1.38
conda install mne=0.18
conda install wget
conda install torch=1.6
conda install tensorboard=2.5
conda install tensorboardX=2.2

```

```bash
conda create -n tinysleepnet_env2 python=3.6
conda activate tinysleepnet_env2
pip install numpy==1.16 pandas==0.24 scikit-learn==0.20 scipy==1.2 matplotlib==3.0 pyEDFlib==0.1.38 mne==0.18 wget torch==1.6 tensorboard==2.5 tensorboardX==2.2
```

```bash
conda create -n tinysleepnet_env3 python=3.6
conda activate tinysleepnet_env3
pip install numpy==1.16 pandas==0.24 scikit-learn==0.20 scipy==1.2 matplotlib==3.0 pyEDFlib==0.1.38 mne==0.18 wget torch==1.6 tensorboard==2.5 tensorboardX==2.2
```


```bash
conda create -n tinysleepnet_env4 python=3.8
conda activate tinysleepnet_env4
pip install numpy pandas scikit-learn scipy matplotlib 
pip install pyEDFlib==0.1.38 mne==0.18 wget 
pip install torch==1.12.0+cu116 torchvision==0.13.0+cu116 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu116
```




### Set a `/tmp` directory during the installation of the packages.

The HPC returns `out of space` error when installing the package `torch`. The `/tmp` directory is used to store the temporary files during the installation of the packages. I set a new directory `/cfs/earth/scratch/dugua001/tmp` to store the temporary files during the installation of the packages.

Create a new directory `/cfs/earth/scratch/dugua001/tmp` if it does not exist:
```bash
mkdir /cfs/earth/scratch/dugua001/tmp
```

Add the following line to `.bashrc`:
```
export TMPDIR=/cfs/earth/scratch/$USER/tmp
```

Apply the changes made to `.bashrc`:
```bash
source ~/.bashrc
```

Test the new `/tmp` directory:
```bash
echo $TMPDIR   # /cfs/earth/scratch/dugua001/tmp
```
## Check the status of the HPC
   
   ```bash
   sinfo
   ```


## test.sh

Add `test.sh` to the home directory:

Then run the following command to submit the job:
```bash
sbatch test.sh
```

## Check the status of the HPC
   
   ```bash
   squeue -u dugua001
   ```


Use salloc to allocate resources for a job:
```bash
salloc --nodes=1 --ntasks-per-node=1 --cpus-per-task=1 --gres=gpu:l40s:1 --time=01:30:00 --partition=earth-4 --constraint=rhel8
```

## 17.10.2024

### Set up the Conda environment for Tinysleepnet on the HPC system.
The CUDA version on the HPC is 11.6.2. The recommended PyTorch version for this CUDA version is 1.12.0. Therefore, build a new Conda environment with the required packages for Tinysleepnet.

```bash
conda create -n tinysleepnet_env4 python=3.8
conda activate tinysleepnet_env4
pip install numpy pandas scikit-learn scipy matplotlib 
pip install pyEDFlib==0.1.38 mne==0.18 wget 
pip install torch==1.12.0+cu116 torchvision==0.13.0+cu116 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu116
pip install tensorboard==2.5 tensorboardX==2.2
```
### Set 'test_gpu2.py' script to test the GPU.

It can find CUDA and GPU. 


## Run the `trainer.py` in the HPC system.

Use `test_trainer.sh` to run the `trainer.py` in the HPC system.

And it returns the following error:

```
Traceback (most recent call last):
  File "trainer.py", line 58, in <module>
    run(
  File "trainer.py", line 29, in run
    train(
  File "/cfs/earth/scratch/dugua001/Tinysleepnet-pytorch/train.py", line 152, in train
    aug_train_x = np.copy(train_x)
  File "<__array_function__ internals>", line 200, in copy
  File "/cfs/earth/scratch/dugua001/.conda/envs/tinysleepnet_env4/lib/python3.8/site-packages/numpy/lib/function_base.py", line 960, in copy
    return array(a, order=order, subok=subok, copy=True)
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (33,) + inhomogeneous part.
```
