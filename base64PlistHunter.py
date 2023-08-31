#!/usr/bin/env python3
# @hoodoer
# hoodoer@bitwisemunitions.dev
#
#
# Pass this an ascii PLIST file that might have base64 encoded binary PLISTs in it, it will extract them for you




import sys
import os
import base64
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET




def extplist(plistfile):
    print("Processing " + plistfile)
    print("")

    tree = ET.parse(plistfile)
    root = tree.getroot()

    def recursiveExtractStrings(element):
        strings = []
        if element.text:
            strings.append(element.text.strip())
        for child in element:
            strings.extend(recursiveExtractStrings(child))
        return strings

    allStrings = recursiveExtractStrings(root)


    tempFileDir = "./plistTemp"

    searchString = "Apple binary property list"

    path = Path(tempFileDir)
    path.mkdir()


    counter = 0
    for string in allStrings:
        # print("Strings dump: " + string)
        counter += 1

        # See if it's a base64 encoded string
        try:
            bplistData = base64.b64decode(string)
        except:
            continue

        outputFile = tempFileDir + '/' + str(counter) + "_testOutput.plist"

        with open(outputFile, "wb") as file:
            file.write(bplistData)


    potentialFiles = os.listdir(tempFileDir)

    for file in potentialFiles:
        filePath = os.path.join(tempFileDir, file)
        result = subprocess.run(["file", filePath],capture_output=True, text=True)
        resultLines = result.stdout.splitlines()

        for line in resultLines:
            if searchString in line:
                print("Successfully extracted Binary PLIST:")
                print(tempFileDir + "/" + file)
                print("")
            else:
                uselessFile = Path(filePath)
                uselessFile.unlink()
    return



if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: %s [plist files]"%sys.argv[0])
        sys.exit(0)
    for pfile in sys.argv[1:]:
        extplist(pfile)