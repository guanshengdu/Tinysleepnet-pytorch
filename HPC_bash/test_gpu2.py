# test_GPU.py

import numpy as np
import matplotlib.pyplot as plt
import os


import torch
import subprocess

def check_cuda():
    print(torch.__version__)
    print("Checking CUDA version and GPU availability in PyTorch...\n")
    # Check if CUDA is available in PyTorch
    if torch.cuda.is_available():
        print(f"CUDA is available!")
        print(f"PyTorch CUDA version: {torch.version.cuda}")
        print(f"Number of GPUs available: {torch.cuda.device_count()}")
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("CUDA is not available.")

def check_nvidia_smi():
    print("\nFetching NVIDIA-SMI information...\n")
    try:
        # Run nvidia-smi command and capture the output
        result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(result.stdout)  # Print the nvidia-smi output
        else:
            print(f"Error running nvidia-smi: {result.stderr}")
    except FileNotFoundError:
        print("nvidia-smi command not found. Please ensure the NVIDIA drivers are installed and accessible.")

if __name__ == "__main__":
    check_cuda()
    check_nvidia_smi()

    print("Checking CUDA status...")
    print(f"CUDA available: {torch.cuda.is_available()}")
    print(f"Number of GPUs: {torch.cuda.device_count()}")

    if torch.cuda.is_available():
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
            print(f"Memory Allocated: {torch.cuda.memory_allocated(i)} bytes")
            print(f"Memory Reserved: {torch.cuda.memory_reserved(i)} bytes")
    else:
        print("CUDA is not available. Please check your environment or allocation.")




    # Optionally, print out the working directory to verify the file locations
    print(f"Current working directory: {os.getcwd()}")




