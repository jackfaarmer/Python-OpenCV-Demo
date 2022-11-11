import sys
from vision import doVision

validExtensions = [".png", ".jpeg", ".jpg"]

print()
print("--- OpenCV DEMO ---")
print("Written by Jack Farmer")
print()
doVision()

imgpath = ""

while (imgpath == ""):
    imgpath = str(input("Enter local filepath with extension (q/Q to quit): "))

    # if Q or q, program exits #
    if ((imgpath.lower() == "q")): 
        sys.exit("\n--- Program exited successfully ---\n")

    if ((imgpath == "")):
        print("\n[!] Please enter a filepath")
        print()
        continue

    extension = False

    #### FIX THIS ####
    for ext in validExtensions:
        if (not imgpath.endswith(ext)):
            continue
        else:
            extension = True
            break
    if (not extension):
        print("\n[!] File extension is not valid")
        print("[!] Please enter a valid file")
        print()
        imgpath = ""
    
    print("\nGot an extension!")


print("Your chosen file is: " + imgpath)
print()

sys.exit("--- Program exited successfuly ---\n")