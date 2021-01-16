# extract
import os

CMDR_RAW_FILES = []

for file in os.listdir("./cmdr_data"):
    if file.endswith(".txt"):
        CMDR_RAW_FILES.append(file)
        print(os.path.join("/cmdr_data", file))

class Extract(object):
    def __init__(self):
        pass
