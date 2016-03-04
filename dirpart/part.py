# Author: Eric Lavesson

import os
from os import path

def discover_files(dir):
    for f in os.listdir(dir):
        if path.isfile(path.join(dir, f)):
            yield f

def place(dir, fname):
    sdir_name = fname[:1].upper()
    full_path = path.join(dir, sdir_name)

    if not path.exists(full_path):
        os.makedirs(full_path)
        print("creating {}".format(full_path))

def part_files(dir):
    files = discover_files(dir)

    for f in files:
        place(dir, f)


