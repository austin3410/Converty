from PIL import Image
import glob
import os
import sys
import logging

cmd_line_args = sys.argv
silent = False
log = False
for cmd_arg in cmd_line_args:
    if cmd_arg in ["--silent", "-s"]:
        silent = True
    elif cmd_arg in ["--help", "-h"]:
        print("Recursive PNG to JPG Usage:\n\n-h or --help - That gives you this.\n-s or --silent - Uses all of the default options, "\
            "doesn't prompt for anything, and starts in the current directory.\n"\
            "-l or --log - Creates a file of all of the converted image names.")
        quit()
    elif cmd_arg in ["--log", "-l"]:
        log = True
        logging.basicConfig(filename='recursive-png-to-jpg.log', format="%(message)s", level=logging.INFO)
    
if silent == False:
    path = input("Input path or press ENTER for current directory:\n")
    if path == "":
        path = os.getcwd()
else:
    path = os.getcwd()

if os.path.exists(path):
    if silent == False:
        print(f"Recursively getting pictures in {path} ...")
    allfiles = [ f for f in glob.glob(path + "/**/*", recursive=True)]
    pictures = [ f for f in glob.glob(path + "/**/*.png", recursive=True)]
else:
    input(f"Path {path} does not exist!")
    quit()
if silent == False:
    print("Found the following pictures:")
    print("\n".join(pictures))
if silent == False:
    x = input("Are you sure you want to convert all of these pictures to '.jpg'?\nY/n: ")
else:
    x = "Y"
if x.upper() == "Y" or x == "":
    if silent == False:
        x = input("Would you like to add a prefix or suffix?\np/s/both/N: ")
        if x.upper() == "S":
            suffix = input("What Suffix would you like to add to the end of the new filename?:\n")
            prefix = ""
        elif x.upper() == "P":
            prefix = input("What Prefix would you like to add to the beginning of the new filename?:\n")
            suffix = ""
        elif x.upper() == "B" or x.upper() == "BOTH":
            prefix = input("What Prefix would you like to add to the beginning of the new filename?:\n")
            suffix = input("What Suffix would you like to add to the end of the new filename?:\n")
        else:
            prefix = ""
            suffix = ""
    else:
        prefix = ""
        suffix = ""
    
    for p in pictures:
        new_p = Image.open(rf"{p}").convert("RGB")
        new_path = os.path.dirname(p)
        filename = os.path.basename(p).replace(".png", f"{suffix}.jpg")
        new_p.save(new_path + f"/{prefix}{filename}")
        if log == True:
            logging.info(p)


    new_allfiles = [ f for f in glob.glob(path + "/**/*", recursive=True)]
    if len(allfiles) + len(pictures) == len(new_allfiles):
        if silent == False:
            print("Finished, converting! All the math checks out, would you like to discard of the old '.png' images?")
            x = input("y/N: ")
            if x.upper() == "Y":
                for p in pictures:
                    os.remove(p)
                print("Garbage collection complete!\nLooks like I'm done here!")
    else:
        msg = f"The coversion finished but the math doesn't check out...\n"\
            f"ALL FILES BEFORE CONVERSION: {len(allfiles)}\nPNG FILES: {len(pictures)}\nALL FILES AFTER CONVERSION: {len(new_allfiles)}\n"\
            f"The correct value for ALL FILES AFTER CONVERSION should be {len(allfiles) + len(pictures)}!\n"\
             "NOTE: If there are already JPG copies in the same direcotry as the original PNG images, this error will occur."
        print(msg)
        if log == True:
            logging.info(msg)


else:
    print("Ok, exiting.")
    quit()
