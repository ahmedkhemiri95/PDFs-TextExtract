import datetime
import numpy as np
import json


def myconverter(o):

    if isinstance(o, datetime.datetime):
        return o.__str__()
    if isinstance(o, np.bool_):
        return o.__str__()


def writeToJSONFile(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, default=myconverter, indent=4)


ports = {
    "data_extraction": 5000
}

PREFIX = "/api"
