import sys
from vision import *

if __name__ == "__main__":

    print("\n--- OpenCV DEMO ---")
    print("Written by Jack Farmer\n")

    # get filepath of desired image
    imgpath = fileIO()

    print("Your chosen file is: " + imgpath + "\n")

    # run face detection
    success = faceDetect(imgpath)

    # exit if an error is encountered
    if (success == False): sys.exit("--- An error occurred! ---")

    # exit if successful
    sys.exit("\n--- Program exited successfuly ---\n")
