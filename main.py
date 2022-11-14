import sys
from vision import *

if __name__ == "__main__":
    print()
    print("--- OpenCV DEMO ---")
    print("Written by Jack Farmer")
    print()

    imgpath = fileIO()

    print("Your chosen file is: " + imgpath)
    print()

    success = doVision(imgpath)
    print()
    if (success == False): sys.exit("--- An error occurred! ---")

    sys.exit("--- Program exited successfuly ---\n")
