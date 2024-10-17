# test.py

import numpy as np
import mne
import matplotlib.pyplot as plt
import os

# Create a numpy array and print its shape
arr = np.random.rand(100, 10)
print(f"Array shape: {arr.shape}")

# Create a basic plot and save it to the working directory
plt.plot(arr[:, 0])
plt.title("Test Plot")
plt.xlabel("Sample Index")
plt.ylabel("Random Values")
plt.savefig("test_plot.png")

# Check MNE version to ensure it is imported correctly
print(f"MNE version: {mne.__version__}")

# Write a message to a text file in the current working directory
with open("test_feedback.txt", "w") as f:
    f.write("Job ran successfully!\n")
    f.write(f"Numpy array shape: {arr.shape}\n")
    f.write(f"MNE version: {mne.__version__}\n")

# Optionally, print out the working directory to verify the file locations
print(f"Current working directory: {os.getcwd()}")
