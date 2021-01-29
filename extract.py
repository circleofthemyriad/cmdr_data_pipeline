# extract
import os
import re
import csv
from datetime import date

from logging import *
from magic import *

CMDR_RAW_FILES     = []
CMDR_CURATED_FILES = []

for file in os.listdir("./cmdr_data"):
    if file.endswith(".txt"):
        CMDR_RAW_FILES.append(file)
        print("Logging - Extract Event: Found Deck List: " + file) # Replace with Logging

for file in os.listdir("./cmdr_metadata"):
    if file.endswith(".csv"):
        CMDR_CURATED_FILES.append(file)

CMDR_RAW_FILES.sort(key=len)
CMDR_CURATED_FILES.sort(key=len)

class Extract(object):
    def __init__(self, filename):
        self.filename = filename.strip(' ')
        self.deckname = self.filename.rstrip('.txt')
        self.metaname = str(self.deckname+"__"+date.today().strftime("%d%m%y")+".csv")

    def isNull(self, list):
        if not list:
            return False
        else:
            return True

    def createDeck(self):
        if os.path.exists('./cmdr_metadata/'+self.metaname):
            os.remove('./cmdr_metadata/'+self.metaname)

        with open('./cmdr_data/'+self.filename) as deck_file:
            for line in deck_file:
                data = tuple(line.split())

                if "Maybeboard" or "Sideboard" in line:
                    card_indeck = False
                else:
                    card_indeck = True

                with open("./cmdr_metadata/"+self.metaname,"a") as decklist:
                    fieldnames = ['Quantity','Card Name','Set','Set Release','Foil','Main Deck']
                    writer     = csv.DictWriter(decklist,fieldnames=fieldnames)

                    card_quantity = data[0]
                    card_name     = re.search(r'\s(.*)\(',line).group(1)
                    card_set      = [i for i in data if i.startswith('(')]
                    card_release  = MTG_SET_DICT[card_set[0].upper()][1]
                    card_foil     = [i for i in data if i.startswith('*')]

                    writer.writerow({'Quantity'   : card_quantity,
                                     'Card Name'  : card_name.strip('\"\'\t\r\n '),
                                     'Set'        : MTG_SET_DICT[card_set[0].upper()][0],
                                     'Set Release': card_release,
                                     'Foil'       : self.isNull(card_foil),
                                     'Main Deck'  : card_indeck
                                    })

            print("Logging - Extract Event: Deck Complete : " + self.deckname)
