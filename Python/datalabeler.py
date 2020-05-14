import pandas as pd
import os
import shutil

metadata = pd.read_csv("./metadata.csv")

def mkdir(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
        return True

def mkdirs(labels):
    mkdir("./data")
   
    for key in labels: 
        key = "./data/" + key
        mkdir(key)

def copyFiles(names, toPath):
    for name in names:
        try:
            name = name + ".jpg"
            shutil.copy(name, toPath)
            print(name)
        except Exception as e:
            print(e)
def moveFiles(metadata):
    for index, row in metadata.iterrows():
        try:
            name = "./" + row["name"] + ".jpg"
            toPath = "./data/" + row["meta.clinical.diagnosis"] + "/" + row["name"] + ".jpg"
            result = shutil.move(name, toPath)
            print(result)
        except Exception as e:
            print(e)
         



labels = metadata["meta.clinical.diagnosis"].value_counts()[0:9]
labels = labels.index.tolist()

metadata = metadata[["name", "meta.clinical.diagnosis"]]
metadata = metadata[metadata["meta.clinical.diagnosis"].isin(labels)]
mkdirs(labels)
moveFiles(metadata)
