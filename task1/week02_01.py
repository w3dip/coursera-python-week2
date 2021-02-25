import os
import tempfile
import argparse
import json
from json.decoder import JSONDecodeError

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

key = args.key
val = args.val

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
mode = 'r+' if os.path.exists(storage_path) else 'w+'
with open(storage_path, mode) as file:
    data = {}
    try:
        data = json.load(file)
    except JSONDecodeError:
        pass
    if key:
        if val:
            new_value = list()
            if key in data.keys():
                new_value = list(data.get(key))
            new_value.append(val)
            data[key] = new_value
            file.seek(0)
            json.dump(data, file)
        else:
            if key in data.keys():
                print(", ".join(map(str, data.get(key))))
            else:
                print("None")
