import sys
import cv2 as cv
from numpy import concatenate
from os import path

'''
Takes an input string with the filepath of a selected file, checks to see if
said file has a valid file extension. If so, the filepath is returned.
Otherwise, the function will continue to ask for a filepath until the user
supplies one or enters Q to quit.

@return imgpath path to image 
'''
def fileIO():

    validExtensions = [".png", ".jpeg", ".jpg"]

    imgpath = ""

    while (imgpath == ""):
        imgpath = str(input("Enter local filepath with extension (q/Q to quit): "))

        # if Q or q, program exits #
        if ((imgpath.lower() == "q")): 
            sys.exit("\n--- Program exited successfully ---\n")

        # if filepath is empty, try again
        if ((imgpath == "")):
            print("\n[!] Filepath cannot be empty!   [!]")
            print("[!] Please enter a valid file.  [!]")

            print()
            continue

        extension = False

        # check to see if file extension is valid
        for ext in validExtensions:
            if (not imgpath.endswith(ext)):
                continue
            else:
                extension = True
                break
        # extension isnt supported, try again
        if (extension == False):
            print("\n[!] File extension is not valid [!]")
            print("[!] Please enter a valid file   [!]")
            print()
            imgpath = ""
            continue

        if ((path.exists(imgpath)) == False):
            print("\n[!] File does not exist!      [!]")
            print("[!] Please enter a valid file [!]")
            print()
            imgpath = ""
            continue

    return imgpath


'''
Given a filepath, runs vision calculations on the supplied image. If the
filepath is empty or if it does not exist, returns false. Otherwise, file is
given to read the image to a Mat and display the image.

@param filepath: path to valid file
@return true if successful, false otherwise
'''
def faceDetect(filepath=""):
    print("Running vision module")

    # check if filepath is valid
    if (filepath == "" or path.exists(filepath) == False): return False
    print("the given filepath is: " + filepath)

    try:
        # read the image to a cv Mat
        img = cv.imread(filepath)
    except:
        print("[ERROR] Failed to read the image")
        return False
    
    try:
        # convert mat to grayscale for face detection
        grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    except:
        print("[ERROR] Could not convert the image to grayscale")
        return False

    try:
        # load model
        faceDetect = cv.CascadeClassifier("facedetect.xml")
    except:
        print("[ERROR] Could not load face detection xml model")
        return False

    try:
        # run model against grayscale image, collect results from the model
        detected = faceDetect.detectMultiScale(grayscale, 1.1, 4)
    except:
        print("[ERROR] Could not run face detection.")
        return False

    # draw a rectangle around each face found
    for (xval,yval,width,height) in detected:
        # pass in image mat, x_init and y_init vals, 
        # x_fin and y_fin vals, color of border, thickness of border
        cv.rectangle(img, (xval, yval), (xval+width, yval+height), (0, 0, 0), 10)

    # bring back original
    origimg = cv.imread(filepath)

    # add text to original and modified images
    origimg = cv.putText(origimg, 'Unmodified', (50, 50),
     cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv.LINE_AA)
    img = cv.putText(img, 'Face Detected', (50, 50),
     cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv.LINE_AA)
    
    # concatenate original with new image (from numpy)
    vertical = concatenate((origimg, img), axis=0)

    # show the face
    cv.startWindowThread()
    cv.imshow(filepath, vertical)
    print("Press any key on the window to close")

    key = cv.waitKey(0)

    return True