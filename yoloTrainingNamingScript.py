import os   #imports functions/tools that allow the program to access user/OS file directory
import re   #imports functions/tools that allow the program to read/write files
import csv  #imports functions/tools that allow the program to read/write .csv files



i = 0       #initializes j counter for setting previous label in for loop
k = 0       #initializes k counter for checking if file is open


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
            f2 = open("train.txt" , "w+")                       #opens new file
            k = 1                                               #sets k counter to stop a new file from being opened/written to       
        modifiedCurrLine = str(currentLine[0])
        modifiedCurrLine = re.sub(",", "" ,modifiedCurrLine)    #removes comma from csv manipulation
        modifiedCurrLine = re.sub("'", "" ,modifiedCurrLine)    #removes comma from csv manipulation
        modifiedCurrLine = modifiedCurrLine.replace("[", "")    #removes bracket from csv manipulation
        modifiedCurrLine = modifiedCurrLine.replace("]", "")    #removes bracket from csv manipulation  
        modifiedCurrLine = "data/obj/" + modifiedCurrLine 
        print(modifiedCurrLine)                                 #prints line its about to write to console
        f2.write(modifiedCurrLine)                              #writes line
        f2.write("\n")                                          #write newline


    if (previousLabel not in currentLine[0]):   #if date is not the same as last lines, add 24 hours to daysCounter
        previousLabel = currentLine[0]              #changes label to new label
f2.close()                                           #closes file once all lines are read, "required"
f.close()                                           #closes file once all lines are read, "required"
