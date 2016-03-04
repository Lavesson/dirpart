# Author: Eric Lavesson

import os
import shutil

from os import path

def discover_files(dir):
    for f in os.listdir(dir):
        if path.isfile(path.join(dir, f)):
            yield f

def place(indir, outdir, fname):
    sdir_name = fname[:1].upper()

    if not path.exists(outdir):
        os.makedirs(outdir)

    full_path = path.join(indir, sdir_name)

    if not path.exists(full_path):
        os.makedirs(full_path)
        shutil.copy2(path.join(indir, fname), path.join(full_path, fname))

def part_files(indir, outdir=""):
    if not outdir:
        outdir = os.getcwd()

    files = discover_files(indir)

    for f in files:
        place(indir, outdir, f)


