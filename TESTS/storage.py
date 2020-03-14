import os
import argparse
import tempfile
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'a') as f: pass
parser = argparse.ArgumentParser()
parser.add_argument('--key', action='store', dest='key', type=str)
parser.add_argument('--value', action='store', dest='value', type=str)
args = parser.parse_args()
if args.key is not None:
    if args.value is not None:
        with open(storage_path, 'a') as f:
            json.dump((args.key, args.value), f)
            f.write('\n')
    else:
        with open(storage_path, 'r') as f:
            lines = f.readlines()
            key_list = filter(lambda x: x[0] == args.key, map(json.loads, lines))
            print(*(item[1] for item in key_list), sep=', ')
