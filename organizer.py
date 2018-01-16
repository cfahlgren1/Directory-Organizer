import os, shutil, re,sys, getopt
import tkinter.filedialog

path = textopen = tkinter.filedialog.askdirectory(mode="r")
files = "files.txt"
count = 0

with open(files) as f:
    for line in f:
        line2 = re.split(" : ", line)
        for file in os.listdir(path):
            if file.endswith(line2[0].strip()):
                if not os.path.exists(path + line2[1].strip()):
                    os.makedirs(path + line2[1].strip())
                shutil.move(os.path.join(path, file), path + line2[1].strip())
                count += 1
    print (str(count) + " files moved!")






