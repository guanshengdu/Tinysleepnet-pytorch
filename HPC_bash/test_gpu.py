# test_GPU.py

import numpy as np
import mne
import matplotlib.pyplot as plt
import os


# Check if CUDA is available
import torch

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
