# SS2_Krak Facial Recognition

## Goals
Create an offline solution that scans through images to detect faces and classify them into corresponding folders of detected individuals.

## Aproach
We will go for a classic step by step approach (no fancy agile stuff).
We first do some reasearch on the existing libraries and solutions to decide about the main structure of the project (RestAPI, simple software, the language we will use, etc.)

### The architecture
The plan is to try the face-recognition library in Python because of its simplicity and if it doesn’t perform well or we need some more functionalities that it doesn’t offer, we switch to FaceNet.
The command line tool will first be implemented for Linux-based systems, with possible extension for Windows in the future.

### TODO
1) Obtain a dataset of photos with faces and photos with no faces, in multiple directories and subdirectories - a few hundred photos, all uniquelly and logically named - IN PROGRESS
  * Online datasets are not exactly what we're looking for, there are usually already extraced faces. Currently trying to build our own dataset, but still looking at online options.
2) Set up the environment and get to know the face-recognition library - IN PROGRESS
3) Recursively loop through the folders, find the images with faces, extract the faces and note where they came from, then save the faces as separate files in the index directory.
4) Perform image classification, group faces of the same person together -> save them in the same folder. 
5) Deploy the program as a command line tool.

### Deployment

### User guide

### Exemples and results
