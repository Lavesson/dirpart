# Author: Eric Lavesson

import os
import shutil

from os import path
import re

_DEFAULT_MISC = "!misc"

def discover_files(dir):
    for f in os.listdir(dir):
        if path.isfile(path.join(dir, f)):
            yield f

def place(indir, outdir, fname, action):
    sdir_name = fname[:1].upper()
    sdir_name = sdir_name if not \
        re.match("^\.", sdir_name) else _DEFAULT_MISC

    if not path.exists(outdir):
        os.makedirs(outdir)

    full_path = path.join(outdir, sdir_name)

    if not path.exists(full_path):
        os.makedirs(full_path)

    action(path.join(indir, fname), path.join(full_path, fname))

def part_files(indir, outdir, move=False, pattern=""):
    files = filter(
        lambda f: re.match(pattern, f), discover_files(indir))

    action = \
        (lambda infile, outfile: shutil.copy2(infile, outfile)) \
            if not move else \
        (lambda infile, outfile: os.rename(infile, outfile))

    for f in files:
        place(indir, outdir, f, action)


