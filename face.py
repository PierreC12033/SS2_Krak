import face_recognition
import numpy
from PIL import Image
import os
from keyring.backends import null


def addFaceToDirectory(pthToSortedFaces, directoryName, pil_image, nameOfNewFile, originalPath, my_face_encoding):
    # Store the img
    pil_image.save(pthToSortedFaces + directoryName + nameOfNewFile + ".png")  # save the face
    # Store the name of the img in the person txt file
    pTxt = open(pthToSortedFaces + directoryName + directoryName + ".txt", "a")
    pTxt.write(nameOfNewFile[1:] + ".png\n")
    pTxt.close()
    # Store the path of the original picture in corresponding file
    pTxt = open(pthToSortedFaces + directoryName + nameOfNewFile + ".txt", "w")
    pTxt.write(originalPath)
    pTxt.close()
    # Store the encoding
    numpy.savetxt(pthToSortedFaces + directoryName + nameOfNewFile + ".enc", my_face_encoding)


def createNewPersonDirectory(pthToSortedFaces, newPersonNumber, pil_image, nameOfNewFile, originalPath, my_face_encoding):
    # If no just create one folder with the first face in it
    # print("There is no faces yet in the directory")
    os.mkdir(pthToSortedFaces + '/person' + str(newPersonNumber))
    # Store the img
    pil_image.save(pthToSortedFaces + '/person' + str(newPersonNumber) + nameOfNewFile + ".png")  # save the face
    # Store the name of the img in the person txt file
    pTxt = open(pthToSortedFaces + '/person' + str(newPersonNumber) + "/person" + str(newPersonNumber) + ".txt", "a")
    pTxt.write(nameOfNewFile[1:] + ".png\n")
    pTxt.close()
    # Store the path of the original picture in corresponding file
    pTxt = open(pthToSortedFaces + '/person' + str(newPersonNumber) + nameOfNewFile + ".txt", "w")
    pTxt.write(originalPath)
    pTxt.close()
    # Store the encoding
    numpy.savetxt(pthToSortedFaces + '/person' + str(newPersonNumber) + nameOfNewFile + ".enc", my_face_encoding)
    # increment for next person
    newPersonNumber += 1


rootdir = '/home/pierrec/Desktop/test_img_reco/IDK'

pth = os.path.dirname(os.path.abspath(__file__)) + "/Photos_copy"
pthToSortedFaces = os.path.dirname(os.path.abspath(__file__)) + "/Faces"

if os.path.exists(pthToSortedFaces):
    newPersonNumber = len(os.listdir(pthToSortedFaces))+1
else:
    newPersonNumber = 1
# Create the directory for faces if not already created
if not (os.path.isdir(pthToSortedFaces)):
    os.mkdir(pthToSortedFaces)



# Scan through the desired file system and analysed the faces if they are not already analysed
for subdir, dirs, files in os.walk(rootdir):
    # Create a copy directory structure if not already existing
    if not (os.path.isdir(pth + subdir[len(rootdir):])):
        os.mkdir(pth + subdir[len(rootdir):])
    # else:
    #     # print("Already copied dir")
    # # print(pth + subdir[len(rootdir):])
    # # print(os.path.basename(subdir))
    # # print(subdir)
    # # print(dirs)
    # # print(files)
    readFiles = null
    txtFileExist = False
    # Did I already scan the images here?
    if not os.path.exists(pth + subdir[len(rootdir):] + '/' + os.path.basename(subdir) + '.txt'):
        # print("the txt file doesn't exist")
        description = open(pth + subdir[len(rootdir):] + '/' + os.path.basename(subdir) + ".txt", "w+")
        for file in files:
            description.write(file + "\n")
        description.close()

    else:
        # print("the txt file exists :")
        txtFileExist = True
        description = open(pth + subdir[len(rootdir):] + '/' + os.path.basename(subdir) + ".txt", "r")
        readFiles = description.readlines()
        description.close()
        a = 0
        for f in readFiles:
            # print("    " + str(a) + " : " + f)
            a += 1
    # Is there new pictures?
    # # print(pth + subdir[len(rootdir):])
    j = 0
    # for each image extract the face locations if it hasn't been treated already
    for file in files:
        isAnalysed = False
        if not readFiles == null:
            if not readFiles.count(str(file + "\n")) == 0:
                # print("file : " + file + " already analysed")
                isAnalysed = True
        if not isAnalysed:
            # print("I never analysed this picture : " + file)
            # add the file to the dir.txt
            if txtFileExist:
                description = open(pth + subdir[len(rootdir):] + '/' + os.path.basename(subdir) + ".txt", "a")
                description.write(file + "\n")
                description.close()
            image = face_recognition.load_image_file(os.path.join(subdir, file))
            face_locations = face_recognition.face_locations(image)
            i = 0
            # for each face location in the image save the face
            for face_location in face_locations:
                top, right, bottom, left = face_location
                if top - 25 > 0:
                    top = top - 25
                if right + 25 < len(image[0]):
                    right = right + 25
                if bottom + 25 < len(image):
                    bottom = bottom + 25
                if left - 25 > 0:
                    left = left - 25

                face_image = image[top:bottom, left:right]
                pil_image = Image.fromarray(face_image)
                nameOfNewFile = '/' + file[:-4] + '_' + str(j) + str(i)
                pil_image.save(pth + subdir[len(rootdir):] + nameOfNewFile + ".png")  # save the face
                # Encoding of the Face
                my_face_encoding = face_recognition.face_encodings(face_image)[0]
                # # print(len(face_recognition.face_encodings(face_image, [[0, len(face_image), 0, len(face_image)]])))
                # Check similarity with existing faces
                # First check if there are any stored faces :
                if len(os.listdir(pthToSortedFaces)) == 0:
                    # If no just create one folder with the first face in it
                    # print("There is no faces yet in the directory")
                    os.mkdir(pthToSortedFaces + '/person' + str(newPersonNumber))
                    # Store the img
                    pil_image.save(pthToSortedFaces + '/person' + str(newPersonNumber) + nameOfNewFile + ".png")  # save the face
                    # Store the name of the img in the person txt file
                    pTxt = open(pthToSortedFaces + '/person' + str(newPersonNumber) + "/person" + str(newPersonNumber) + ".txt", "a")
                    pTxt.write(file[:-4] + '_%d%d.png\n' % (j, i))
                    pTxt.close()
                    # Store the path of the original picture in corresponding file
                    pTxt = open(pthToSortedFaces + '/person' + str(newPersonNumber) + nameOfNewFile + ".txt", "w")
                    pTxt.write(os.path.join(subdir, file))
                    pTxt.close()
                    # Store the encoding
                    numpy.savetxt(pthToSortedFaces + '/person' + str(newPersonNumber) + nameOfNewFile + ".enc", my_face_encoding)
                    # increment for next person
                    newPersonNumber += 1
                else:
                    dirsfc = os.listdir(pthToSortedFaces)
                    found = False
                    y = 0
                    # print("dirsfc")
                    # print(dirsfc)
                    while not found and y != len(dirsfc):
                        # I check the next folder for recognition If it is recognized I am happy
                        #  img_reco/SS2_Krak-main/Faces /    person1      /     person1     .txt
                        pTxt = open(pthToSortedFaces + '/' + dirsfc[y] + '/' + dirsfc[y] + ".txt", "r")
                        readFacesFile = pTxt.readlines()
                        pTxt.close()
                        loadedListOfEncoded = []
                        for f2 in readFacesFile:
                            # print(pthToSortedFaces + '/' + dirsfc[y] + '/' + f2[:-1])
                            loadedListOfEncoded.append(numpy.loadtxt(pthToSortedFaces + '/' + dirsfc[y] + '/' + f2[:-4] + "enc"))

                        # try to match faces
                        # print(face_recognition.face_distance(loadedListOfEncoded, my_face_encoding))
                        # # print(str(top)+" "+str(right)+" "+str(bottom)+" "+str(left))
                        # print(my_face_encoding)
                        # print(face_recognition.compare_faces(loadedListOfEncoded, my_face_encoding, 0.3))
                        if face_recognition.compare_faces(loadedListOfEncoded, my_face_encoding, 0.5)[0]:
                            found = True
                            y -= 1
                        y += 1
                    if found:
                        # someone look similar to my face, I will get into his directory
                        addFaceToDirectory(pthToSortedFaces, '/' + dirsfc[y], pil_image, nameOfNewFile, os.path.join(subdir, file), my_face_encoding)
                    else:
                        createNewPersonDirectory(pthToSortedFaces, newPersonNumber, pil_image, nameOfNewFile, os.path.join(subdir, file), my_face_encoding)
                        newPersonNumber += 1
                    my_face_encoding = null
                i = i + 1
            j = j + 1
