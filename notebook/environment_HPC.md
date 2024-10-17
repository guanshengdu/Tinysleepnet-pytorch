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
module load gcc/9.4.0-pe5.34 miniconda3/4.12.0 lsfm-init-miniconda/1.0.0 # USS/2020: 4.8.2 (GCC 7.3.0)
module load gcc/7.3.0 miniconda3/4.8.2 lsfm-init-miniconda/1.0.0 # Load in USS/2022: 4.12.0 (GCC 9.4.0-pe5.34)
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

## Explanation of the `.condarc` file:
<summary>details of '.condarc'</summary>
The recommendation to configure Conda using a `.condarc` file, especially with user-specific settings in the HPC environment, provides several important benefits. Let me explain why this configuration is helpful and why you should like this approach:

### 1. **Environment Storage in User Directory**
By configuring `envs_dirs` to store environments in the directory `/cfs/earth/scratch/$USER/.conda/envs`, you're ensuring that all your Conda environments are stored in your **personal scratch space**. Here’s why this is beneficial:

- **Isolation and Control**: You avoid interfering with the system-wide Conda environments and configurations. This gives you complete control over your environments, allowing you to install, update, or delete packages as needed without affecting other users.
- **No Disk Quota Issues in Home Directory**: Scratch space (`/cfs/earth/scratch/$USER/`) is typically designed to handle larger, temporary data in HPC systems, and is often less restrictive in terms of storage quota than your `$HOME` directory. This is especially important if you're creating multiple environments or large environments with many dependencies.
- **Faster I/O Performance**: The scratch directory is usually optimized for faster I/O operations, which means creating, modifying, and using Conda environments will be more efficient compared to storing them in slower, heavily used directories like `/home`.

### 2. **Centralized Package Cache**
The `pkgs_dirs` setting points to `/cfs/earth/scratch/$USER/.conda/pkgs`, where downloaded Conda packages are stored. This configuration brings multiple benefits:

- **Package Reuse**: When you install a package in different environments, Conda will reuse packages from this directory instead of downloading them again. This saves time and bandwidth, and also ensures you’re using consistent versions of packages across environments.
- **Efficient Space Usage**: By centralizing your package cache in the scratch space, you minimize disk usage. Instead of each environment containing its own copy of installed packages, Conda will link to the centralized package cache when creating new environments, reducing redundancy.

### 3. **Channel Configuration**
The recommended configuration sets two important channels:
- **`conda-forge`**: This channel contains a vast collection of open-source packages and is often preferred for its up-to-date and well-maintained packages.
- **`defaults`**: This is the default Conda channel, which also provides essential packages.

Having these channels set in your `.condarc` file means Conda will search these repositories in the correct order. Setting the `channel_priority: strict` enforces strict priority, ensuring that if a package is available in `conda-forge`, it will use that version over one from `defaults`. This helps avoid conflicts and ensures that the versions of packages you’re installing are consistent with the main source.

### 4. **Customizing Environment Prompt**
The `env_prompt: '({default_env}) '` configuration provides a clearer way to identify which environment you’re currently using by displaying the name in your terminal prompt. This can help avoid confusion when switching between different Conda environments, especially when working in different environments for different projects.

### 5. **Turning Off Base Environment Auto-Activation**
Setting `auto_activate_base: false` ensures that the base Conda environment doesn’t activate automatically when you log in or start a new shell session. This is generally preferred in an HPC environment for several reasons:

- **Less Overhead**: The base environment can come with pre-installed packages that you don’t need for every session. Not auto-activating the base environment keeps things lightweight and lets you manually activate specific environments when needed.
- **Avoid Conflicts**: If you’re working on multiple projects or jobs that use different environments, automatically activating the base environment can lead to unwanted conflicts. This setting helps you maintain clean, project-specific environments.

### 6. **Improved Customization and Portability**
By configuring Conda through the `.condarc` file, you gain greater control over how Conda behaves for your user account. If you move to a different HPC system or workstation, you can bring this file with you, ensuring consistency in your Conda behavior across systems.

---

### Summary of Benefits
- **Efficient use of storage** by placing environments and package cache in scratch space.
- **Improved package management** with centralized storage and strict channel priority.
- **Avoids base environment conflicts**, improving workflow flexibility.
- **Clearer environment usage** with a custom environment prompt.
- **Customizable and portable** configuration, allowing you to have consistent behavior across systems.

This configuration is well-suited for HPC environments where disk space and performance optimizations are critical, and where user-specific customizations help ensure smoother, conflict-free workflows.

Let me know if you have more questions or need further clarification!



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
pip install numpy==1.16 pandas==0.24 scikit-learn==0.20 scipy==1.2 matplotlib==3.0 pyEDFlib==0.1.38 mne==0.18 wget torch==1.6 tensorboard==2.5 tensorboardX==2.2
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



## Using HPC, from ChatGPT

Yes, you’re right. HPC systems typically require you to load Conda environments differently than on your local machine because HPC environments often use **modules** for software management. These modules allow different versions of software to coexist on the same system, making it necessary to load the appropriate environment management system, such as Conda.

Here are more details on how to handle this:

### Step 1: Check for Conda Availability

HPC clusters often have Conda (or Miniconda/Anaconda) pre-installed but may use a **module system** (like `module load`) to access it. Here's how you can work with it:

1. **Check available modules**: Run the following command to list the available modules on the login node:

   ```bash
   module avail
   ```

   Look for something related to **Anaconda** or **Miniconda** in the output list. For example, you might see something like:

   ```
   anaconda/2020.11
   miniconda/4.8.3
   ```

2. **Load the Conda module**: If you see a Conda-related module, load it using the following command (adjusting the version to what’s available on your cluster):

   ```bash
   module load anaconda/2020.11
   ```

3. **Verify that Conda is loaded**: After loading the module, check if Conda is now accessible by running:

   ```bash
   conda --version
   ```

   If this command shows the version of Conda, you are good to go.

### Step 2: Create and Activate a Conda Environment

Once the Conda module is loaded, you can proceed with creating and managing your environments:

1. **Create a Conda environment** (if you haven’t already):

   ```bash
   conda create -n myenv python=3.8
   ```

   This will create a new Conda environment called `myenv`.

2. **Activate the Conda environment**:

   Instead of simply running `conda activate myenv`, HPC systems often require an extra step to ensure the environment is activated correctly. After loading the Conda module, use:

   ```bash
   source activate myenv
   ```

   If this does not work directly, try:

   ```bash
   conda activate myenv
   ```

### Step 3: Modify the Slurm Job Script

Once you have the Conda environment set up, you need to make sure it’s activated within the Slurm job script. Here's an example of how to adjust the script to load and activate the Conda environment:

```bash
#!/bin/bash
#SBATCH --job-name=my_conda_job    # Job name
#SBATCH --output=output.txt        # Output log
#SBATCH --error=error.txt          # Error log
#SBATCH --time=01:00:00            # Time limit (hh:mm:ss)
#SBATCH --ntasks=1                 # Number of tasks
#SBATCH --cpus-per-task=4          # Number of CPU cores
#SBATCH --mem=16G                  # Memory allocation

# Load the Anaconda module (adjust to the available version on your cluster)
module load anaconda/2020.11

# Activate your Conda environment
source activate myenv

# Run your Python script
python myscript.py
```

In this script:
- The `module load anaconda/2020.11` command loads Conda.
- The `source activate myenv` or `conda activate myenv` command activates the environment.
- Then, your Python script runs in the environment you've set up.

### Step 4: Ensure Environment Consistency

If you plan to use the same environment across multiple jobs, it's good practice to store your Conda environment in a directory that's accessible across all nodes (like in a shared `/home` or `/scratch` directory). This way, it’s available to both the login nodes and compute nodes, ensuring consistency across jobs.

You can set the location of the Conda environments globally using:

```bash
conda config --add envs_dirs /home/your_username/conda_envs
```


This ensures that all environments are stored in `/home/your_username/conda_envs`, which can be accessed by both the login and compute nodes.

### Troubleshooting Tips

- **Permissions**: Make sure you have write permissions to the directories where you create the Conda environments.
- **Environment Conflicts**: If you run into issues with packages, try creating a minimal Conda environment or use `conda env export` and `conda env create` to replicate your local environment on the cluster.
- **Module Compatibility**: If your cluster uses modules for specific libraries or compilers (e.g., `gcc`, `mpi`), make sure to load the appropriate ones in your job script before activating Conda.

### Summary
- Use `module load anaconda` to load Conda.
- Activate the Conda environment using `source activate myenv`.
- Submit the job with Slurm, ensuring that the Conda environment is activated in your job script.

Let me know if you need any more details or clarification!


## Load the Conda environment and install the required packages in the HPC system.

If you have created a Conda environment in the HPC system, you can use it to run your code in two main scenarios: interactively (directly from the terminal) or through a job scheduler like Slurm. Here's how you can use your Conda environment in both situations:

### 1. **Using the Conda Environment Interactively**

When you're logged into the HPC system through SSH and working interactively (not submitting jobs), you can use your Conda environment like this:

1. **Activate the Conda Environment**:
   After you have created your Conda environment, activate it with:

   ```bash
   # Activate your environment (replace 'myenv' with your environment name)
   conda activate myenv
   ```

2. **Run Your Code**:
   Once the environment is active, you can run your code interactively. For example, if your code is a Python script:

   ```bash
   python myscript.py
   ```

3. **Deactivate the Environment**:
   Once you're done using the environment, you can deactivate it:

   ```bash
   conda deactivate
   ```

### 2. **Using the Conda Environment in a Slurm Job**

To run your code on the compute nodes using Slurm, you need to ensure that your Conda environment is activated within the job script. Here's how to set it up:

#### Step-by-Step Guide for a Slurm Job:

1. **Create Your Slurm Job Script**:
   Create a bash script (let's say `jobscript.sh`) to submit your job. Inside this script, you need to activate your Conda environment and run your code. Here is an example:

   ```bash
   #!/bin/bash
   #SBATCH --job-name=my_conda_job   # Job name
   #SBATCH --output=output.txt       # Output log
   #SBATCH --error=error.txt         # Error log
   #SBATCH --time=01:00:00           # Time limit (hh:mm:ss)
   #SBATCH --ntasks=1                # Number of tasks (usually 1)
   #SBATCH --cpus-per-task=4         # Number of CPU cores
   #SBATCH --mem=16G                 # Memory allocation

   # Load necessary modules if required (skip if not needed)
   # module load anaconda

   # Activate your Conda environment
   source /home/username/software/miniconda3/bin/activate myenv

   # Run your Python script
   python myscript.py

   # Deactivate the environment (optional, but good practice)
   conda deactivate
   ```

   **Explanation**:
   - The `source` command activates your Conda environment.
   - Once the environment is active, you can run your Python code or any other command that uses the environment.
   - At the end of the job, you deactivate the environment (optional, but it helps keep things clean).

2. **Submit the Job**:
   Once the job script (`jobscript.sh`) is prepared, submit it to the Slurm scheduler using the `sbatch` command:

   ```bash
   sbatch jobscript.sh
   ```

   This will submit the job to the Slurm scheduler, and Slurm will allocate the required resources to run your job.

3. **Check Job Status**:
   You can check the status of your job using:

   ```bash
   squeue -u your_username
   ```

   This will show you the list of your jobs and their current status in the queue.

4. **Review Output and Errors**:
   After the job is finished, check the output and error files (`output.txt` and `error.txt`) to see the results and any issues encountered during execution.

#### Example Slurm Script for Parallel Jobs:
If you want to run parallel tasks (e.g., multi-core or multi-node), you can modify the `SBATCH` directives accordingly. Here’s an example for a parallel job:

```bash
#!/bin/bash
#SBATCH --job-name=my_parallel_conda_job
#SBATCH --output=output.txt
#SBATCH --error=error.txt
#SBATCH --time=02:00:00
#SBATCH --ntasks=4                  # Number of tasks (parallel jobs)
#SBATCH --cpus-per-task=4           # CPUs per task
#SBATCH --mem=32G                   # Memory allocation
#SBATCH --partition=compute         # Specify partition if needed

# Activate your Conda environment
source /home/username/software/miniconda3/bin/activate myenv

# Run a Python script in parallel
mpirun -np 4 python my_parallel_script.py

# Deactivate the environment
conda deactivate
```

### Key Points to Remember:

- **Environment Activation**: Always ensure that you activate your Conda environment using `source activate` or `conda activate` in your job script before running your code.
  
- **System Modules**: If your HPC system uses a module system, ensure that you are loading the correct modules (if needed) before activating Conda. For example, if the HPC cluster uses modules for software management (e.g., `module load anaconda`), include that command before activating your environment.

- **Path to Conda**: Ensure that you use the full path to `conda activate` if it’s installed in your user directory (as shown in the examples).

- **Resource Requests**: Adjust the resource requests (`#SBATCH` lines) in your Slurm script according to the needs of your job. For instance, if your job requires more memory, more cores, or needs to run for a longer duration, modify the relevant lines in your script (e.g., `--mem`, `--cpus-per-task`, and `--time`).

### Summary:
1. **Interactive Use**:
   - SSH into the HPC system, activate the Conda environment, and run your code.
   
2. **Submitting Jobs**:
   - Write a Slurm job script, activate the Conda environment within the script, and run your code.
   - Submit the job using `sbatch`.

By following these steps, you can effectively use your Conda environment on an HPC cluster, both interactively and through job submission. Let me know if you need more details or run into any issues!


