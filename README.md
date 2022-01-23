# SS2_Krak Facial Recognition

## Goals
Design and implement a command line tool that:
* browses through a collection of photos in the filesystem (multiple directories, recursively),
* extract face images from the original photos and stores them in an index directory as separate files,
* groups faces of the same person together,
* with each face it stores information about what photo it came from.


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
    

The program detects and extracts faces from all images. The extracted faces are saved in the Photos_copy directory, which has the same structure as the original directory of the photos specified when starting the program. In each directory / subdirectory in the Photos_copy directory you can find the extracted faces, which were found in the images in the coorresponding directory / subdirectory in the original photos file structure. In the same place you can also find a .txt file, in which you can find the names of all the images found in the corresponding subdirectory in the original file structure. This is needed for the program to know, which photos have already been analyzed when rerunning the program, so that it doesn't analyze the same pictures again.

The extracted faces are then analyzed and classified according to which person the face belongs to. You can find the classified faces in the Faces directory. For each new detected person, a new subdirectory is created, so each unique person has its own unique directory, called PersonX. In such a directory, for example /Faces/person1, you can find all the extracted faces of a certain person and also other files. For each image of a face, there is an encoding file with the exact same name as the image of the face, but with .enc extension. This file contains the encoding of this face, so that it doesn't have to be encoded again in the future and it also assures quick comparison with other face encodings, when trying to classifiy faces. For each face image, there is also a text file with the same name as the face image, but with a .txt extension. In this file you can find the path to the original image where this face was extracted from. 

The Photos_copy and Faces directories can be found in the same directory where the program was run from.

The program only works on .jpg images. After processing, the images are saved as .png files (because of the usage of a certain library), but let that not deceive you. All the images in the original directory of pictures you pass to the program, must have a .jpg extension.

During processing, every face detected will be displayed as '*', every file analysed as ':' , every folder scanned as 'O'.

### Known issues
A warning can appear at the beginning of the execution, please ignore it, it won't affect the results.

Sometimes the message :"ERROR FACE DETECTED BUT NO ENCODING POSSIBLE" can appear, this mean that a face has been detected but the program was unable to encode it. Resulting in the impossibility of the classification for this specific face. 

If a picture is corrupted or empty it might interrupt the program.  

### Possible future developments
* Multithreading
* Improvement of the classification accuracy by reclassification of already classified images
* Improvement of the encoding of the faces, so that all of the faces can be encoded with no (or very rare) exceptions

### Licensing

GNU GPL 3.0
