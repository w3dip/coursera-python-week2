import os
import tempfile
import argparse

parser = argparse.ArgumentParser()
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as f:
    pass