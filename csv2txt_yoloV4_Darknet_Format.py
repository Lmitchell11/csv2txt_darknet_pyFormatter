#Liam Mitchell
#CSV to Text File conversion script for formatting AI training data from Kaggle - "Self-Driving Cars Archive" - Formats for Darknet Yolov4 training
#4/03/2022

import os   #imports functions/tools that allow the program to access user/OS file directory
import re   #imports functions/tools that allow the program to read/write files
import csv  #imports functions/tools that allow the program to read/write .csv files



i = 0       #initializes j counter for setting previous label in for loop
k = 0       #initializes k counter for checking if file is open
darknetArray = []

img_width = 480     #image pixels width size
img_height = 300    #image pixels height size


"""Setup your PATH below correspondingly, and insure that this 'python.exe' and 'labels_train.csv' are in a seperately contained folder...
or you'll be mad for a second"""

f = open("C:/Users/runes/Downloads/Self-Driving Cars_archive/csv2txt_darknet_pyFormatter/labels_train.csv", "r+")    #Comment above
next(f)                                     #skips first line because that is where the HEADER information is
for line in f:                              #reads line by line
    currentLine = line.split(",")           #splits up line into array, seperates based off commas (CSV format)

    if (i < 1):                             #uses j counter to set first label from 2nd line
        previousLabel = currentLine[0]      #sets first label so the if statements below work
        i = i + 1                           #increment, and never execute again

    if (previousLabel in currentLine[0]):                   #checks to see if label is the same as the last line
        if (k == 0):                                            #counter that checks to see if file is open
            filenameStr = str(currentLine[0][:-4])              #removes .jpeg file extension so its rewritable beyond filename
            filenameStr = filenameStr + ".txt"                  #changes file extension to .txt
            f2 = open(filenameStr , "w+")                       #opens new file
            k = 1                                               #sets k counter to stop a new file from being opened/written to

        darknetArray = []
        x_center = (int(currentLine[1]) + int(currentLine[2])) / 2
        y_center = (int(currentLine[3]) + int(currentLine[4])) / 2
        width = int(currentLine[2]) - int(currentLine[1])
        height = int(currentLine[4]) - int(currentLine[3])
        x_center /= img_width 
        y_center /= img_height 
        width    /= img_width 
        height   /= img_height 
        darknetArray.append("{:.3f} {:.3f} {:.3f} {:.3f}".format(x_center, y_center, width, height))

        
        modifiedCurrLineLast = currentLine[5].rstrip()
        modifiedCurrLineLast = int(modifiedCurrLineLast)
        modifiedCurrLineLast = modifiedCurrLineLast - 1
        modifiedCurrLine = str(currentLine[:-1])
        modifiedCurrLine = (str(modifiedCurrLineLast) + " " + str(darknetArray))
        modifiedCurrLine = re.sub(",", "" ,modifiedCurrLine)    #removes comma from csv manipulation
        modifiedCurrLine = re.sub("'", "" ,modifiedCurrLine)    #removes comma from csv manipulation
        modifiedCurrLine = modifiedCurrLine.replace("[", "")    #removes bracket from csv manipulation
        modifiedCurrLine = modifiedCurrLine.replace("]", "")    #removes bracket from csv manipulation  
        print(modifiedCurrLine)                                 #prints line its about to write to console
        f2.write(modifiedCurrLine)                              #writes line
        f2.write("\n")                                          #write newline

                                                                #IF ANYONE ACTUALLY KNOWS HOW TO USE THE REGEX PATTERN PLEASE FEEL FREE TO ROAST MY CODE

    if (previousLabel not in currentLine[0]):   #if date is not the same as last lines, add 24 hours to daysCounter
        f2.close()                                  #closes file once all lines are read, "required"
        previousLabel = currentLine[0]              #changes label to new label
        k = 0                                       #resets counter so next new file can be opened
f.close()                                           #closes file once all lines are read, "required"
