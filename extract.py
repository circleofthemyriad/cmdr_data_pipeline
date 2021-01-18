# extract
import os
import re
import csv
from datetime import date

from magic import *

CMDR_RAW_FILES = []

for file in os.listdir("./cmdr_data"):
    if file.endswith(".txt"):
        CMDR_RAW_FILES.append(file)
        print("Logging - Extraction Event: Found " + file) # Replace with Logging

CMDR_DECKS_NUM = len(CMDR_RAW_FILES)

class Extract(object):
    def __init__(self, filename):
        self.filename = filename
        self.deckname = filename.rstrip('.txt')
        self.metaname = str(self.deckname+"_"+date.today().strftime("%d%m%y")+".csv")

    def createDeck(self):
        if os.path.exists('./cmdr_metadata/'+self.metaname):
            os.remove('./cmdr_metadata/'+self.metaname)
            
        with open("./cmdr_data/"+self.filename) as deck_file:
            for line in deck_file:
                data = tuple(line.split())
                print("Logging - Card Event: " + self.deckname + " Entry: " + str(data)) # Replace with Logging

                with open("./cmdr_metadata/"+self.metaname,"a") as decklist:
                    fieldnames = ['Card Name','Set','Set Release','Quantity']
                    writer     = csv.DictWriter(decklist,fieldnames=fieldnames)

                    card_quantity = data[0]
                    card_name     = re.search(r'x(.+?)[^(]',line).group(1)
                    card_set      = [i for i in data if i.startswith('(')]
                    card_release  = MTG_SET_DICT[card_set[0].upper()]

                    writer.writerow({'Card Name'  : card_name,
                                     'Set'        : card_set,
                                     'Set Release': card_release,
                                     'Quantity'   : card_quantity
                                    })
