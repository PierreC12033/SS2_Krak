# SS2_Krak Facial Recognition

## Goals
Create an offline solution that scans through images to detect faces and classify them into corresponding folders of detected individuals.

## Aproach
We will go for a classic step by step approach (no fancy agile stuff).
We first do some reasearch on the existing libraries and solutions to decide about the main structure of the project (RestAPI, simple software, the language we will use, etc.)

### The architecture
The plan is to try the face-recognition library in Python because of its simplicity and if it doesn’t perform well or we need some more functionalities that it doesn’t offer, we switch to FaceNet.
The command line tool will first be implemented for Linux-based systems, with possible extension for Windows in the future.

### Installation of face_recognition library
Installation requirements:

Python 3.3+ or Python 2.7
macOS or Linux (Windows not officially supported, but might work)

Installing on Mac or Linux:

First, make sure you have dlib already installed with Python bindings:

    https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf

Then, install this module from pypi using pip3 (or pip2 for Python 2):

    pip3 install face_recognition

If you are having trouble with installation, you can also try out a
pre-configured VM: https://medium.com/@ageitgey/try-deep-learning-in-python-now-with-a-fully-pre-configured-vm-1d97d4c3e9b


### TODO
1) Obtain a dataset of photos with faces and photos with no faces, in multiple directories and subdirectories - a few hunder photos - DONE
  * After a thorough search for datasets on the internet we decided to create our own dataset of our own vacation photos.
3) Set up the environment and get to know the face-recognition library - DONE
4) Recursively loop through the folders, find the images with faces, extract the faces - DONE
5) Save information about the location of extracted faces in the original photos - DONE
6) Perform image classification, group faces of the same person together -> save them in the same folder - TO OPTIMIZE
8) Deploy the program as a command line tool.

### Deployment

### User guide

### Exemples and results
