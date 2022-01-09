# SS2_Krak Facial Recognition

## Goals
Create an offline solution that scans through images to detect faces and classify them into corresponding folders of detected individuals.

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

### Usage
Example usage:

python face.py [full path to a folder with images] 

You can also use the -help option to display a short helpful description of the program:

python face.py -help

To delete all the presaved encodings and therefore process all the images again, you can use the -reset option:

python face.py [full path to a folder with images] -reset

The program only works on .jpg images.

During processing, every face detected will be displayed as '*', every file analysed as ':' , every folder scanned as 'O'.

