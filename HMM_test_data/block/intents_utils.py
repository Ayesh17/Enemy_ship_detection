import sys
import csv
import math
import os
import numpy as np
from typing import Tuple



# New representation for intents/models as a nested dictionary
ramModel = {
  'name' : 'RAM',
  'hmmName': 'RAM_hmm_mn',
  'encoderName': 'RAM_encoder',
  'ID' : 1,
  'HII_ID': 6
}
blockModel = {
  'name' : 'BLOCK',
  'hmmName': 'BLOCK_hmm_mn',
  'encoderName': 'BLOCK_encoder',
  'ID' : 5,
  'HII_ID': 8
}
herdModel = {
  'name' : 'HERD',
  'hmmName': 'HERD_hmm_mn',
  'encoderName': 'HERD_encoder',
  'ID' : 7,
  'HII_ID': 7
}

benignModel = {
  'name' : 'BENIGN',
  'hmmName': 'BENIGN_hmm_mn',
  'encoderName': 'BENIGN_encoder',
  'ID' : 3,
  'HII_ID': 1
}

crossModel = {
  'name' : 'CROSS',
  'hmmName': 'CROSS_hmm_mn',
  'encoderName': 'CROSS_encoder',
  'ID' : 9,
  'HII_ID': 5
}

overtakeModel = {
  'name' : 'OVERTAKE',
  'hmmName': 'OVERTAKE_hmm_mn',
  'encoderName': 'OVERTAKE_encoder',
  'ID' : 11,
  'HII_ID': 4
}

headonModel = {
  'name' : 'HEADON',
  'hmmName': 'HEADON_hmm_mn',
  'encoderName': 'HEADON_encoder',
  'ID' : 13,
  'HII_ID': 3
}

stationaryModel = {
  'name': 'STATIONARY',
  'hmmName': 'STATIONARY_hmm_mn',
  'encoderName': 'STATIONARY_encoder',
  'ID': 15,
  'HII_ID': 2
}

transitModel = {
  'name': 'TRANSIT',
  'hmmName': 'TRANSIT_hmm_mn',
  'encoderName': 'TRANSIT_encoder',
  'ID': 17,
  'HII_ID': 17
}

waitModel = {
  'name' : 'WAIT',
  'hmmName': 'WAIT_hmm_mn',
  'encoderName': 'WAIT_encoder',
  'ID': 19,
  'HII_ID': 19
}

intentsDict = {
  'RAM': ramModel,
  'BLOCK': blockModel,
  'HERD': herdModel,
  'BENIGN': benignModel,
  'CROSS': crossModel,
  'OVERTAKE': overtakeModel,
  'HEADON': headonModel,
  'STATIONARY': stationaryModel,
  'TRANSIT': transitModel,
  'WAIT': waitModel
}

behPhaseHIIDict = {
    0: 'NONE',
    1: 'WAIT',
    2: 'TRANSIT',
    3: 'EXECUTE',
    4: 'COMPLETE'
}

# Arrays for missing mover and unknown probabilities
MM_label = -1
MM_probs = [MM_label]*len(intentsDict)
UNK_label = -2
UNK_probs = [UNK_label]*len(intentsDict)
UNK_ID = 0

def getNamesHMMs(intentsDict):
    namesHMMs = []
    for name, model in intentsDict.items():
        namesHMMs.append(model['hmmName'])
    return namesHMMs

def getUNRIntentIDFromHIIIntentID(intentsDict, label):
    for model in intentsDict.values():
        if model['HII_ID'] == label:
            return model['ID']
    return -5

def getUNRIntentNameFromUNRIntentID(intentsDict, unrID):
    for model in intentsDict.values():
        if model['ID'] == unrID:
            return model['name']
    return 'empty'

def getUNRIntentIDList(intentsDict):
    intentList = []
    for model in intentsDict.values():
        intentList.append(str(model['ID']))
    return intentList

