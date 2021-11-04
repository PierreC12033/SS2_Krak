# SS2_Krak Facial Recognition

## Goals
Create an offline solution that scans through images to detect faces and classify them into corresponding folders of detected individuals.

## Aproach
We will go for a classic step by step approach (no fancy agile stuff).
We first do some reasearch on the existing libraries and solutions to decide about the main structure of the project (RestAPI, simple software, the language we will use, etc.)

### The architecture
The plan is to try the face-recognition library in Python because of its simplicity and if it doesn’t perform well or we need some more functionalities that it doesn’t offer, we switch to FaceNet. 

### TODO
1) Set up a dataset of photos with faces and photos with no faces, in multiple directories and subdirectories - a few hundred photos, all uniquelly and logically named.
2) Recursively loop through the folders, find the images with faces, extract the faces and note where they came from, then save the faces as separate files in the index directory.
3) Perform image classification, group faces of the same person together -> save them in the same folder. 
4) Deploy the program as a command line tool.

### Timeline


### Deployment

### User guide

### Exemples and results
