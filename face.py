
import face_recognition
from PIL import Image
import os


rootdir = '/home/klara/Desktop/AGH/Project/Photos'

pth = os.path.dirname(os.path.abspath(__file__)) + "/Photos_copy"

for subdir, dirs, files in os.walk(rootdir):

    # Create a copy directory structure
    os.mkdir(pth + subdir[len(rootdir):])

    j = 0
    # for each image extract the face locations
    for file in files:

        #print(os.path.join(subdir, file))
        image = face_recognition.load_image_file(os.path.join(subdir, file))
        face_locations = face_recognition.face_locations(image)

        i = 0
        # for each face location in the image save the face
        for face_location in face_locations:

            top, right, bottom, left = face_location
            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            pil_image.save('face%d%d.png' % (j,i)) # save the face
            i = i + 1

        j = j + 1





