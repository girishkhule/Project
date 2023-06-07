import os
import string

# Importing the necessary modules

# Creating the directory Structure

# Check if the "dataSet" directory exists, and create it if it doesn't
if not os.path.exists("dataSet"):
    os.makedirs("dataSet")

# Check if the "trainingData" directory exists within "dataSet", and create it if it doesn't
if not os.path.exists("dataSet/trainingData"):
    os.makedirs("dataSet/trainingData")

# Check if the "testingData" directory exists within "dataSet", and create it if it doesn't
if not os.path.exists("dataSet/testingData"):
    os.makedirs("dataSet/testingData")

# Making folder 0 (i.e blank) in the training and testing data folders respectively
for i in range(0):
    # Check if the folder with name "i" exists within "trainingData", and create it if it doesn't
    if not os.path.exists("dataSet/trainingData/" + str(i)):
        os.makedirs("dataSet/trainingData/" + str(i))

    # Check if the folder with name "i" exists within "testingData", and create it if it doesn't
    if not os.path.exists("dataSet/testingData/" + str(i)):
        os.makedirs("dataSet/testingData/" + str(i))

# Making Folders from A to Z in the training and testing data folders respectively

# Iterate over each uppercase letter in the string.ascii_uppercase string
for i in string.ascii_uppercase:
    # Check if the folder with letter "i" exists within "trainingData", and create it if it doesn't
    if not os.path.exists("dataSet/trainingData/" + i):
        os.makedirs("dataSet/trainingData/" + i)
    
    # Check if the folder with letter "i" exists within "testingData", and create it if it doesn't
    if not os.path.exists("dataSet/testingData/" + i):
        os.makedirs("dataSet/testingData/" + i)
