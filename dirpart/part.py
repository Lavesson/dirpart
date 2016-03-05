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

def place(fname, action, args):
    outdir = args["outdir"]
    indir = args["indir"]

    sdir_name = fname[:1].upper()
    sdir_name = sdir_name if not \
        re.match("^\.", sdir_name) else args["special"]

    if not path.exists(outdir):
        os.makedirs(outdir)

    full_path = path.join(outdir, sdir_name)

    if not path.exists(full_path):
        os.makedirs(full_path)

    action(path.join(indir, fname), path.join(full_path, fname))

def part_files(**args):
    if not "special" in args or not args["special"]:
        args["special"] = _DEFAULT_MISC

    files = filter(
        lambda f: re.match(args["pattern"], f),
        discover_files(args["indir"]))

    action = \
        (lambda infile, outfile: shutil.copy2(infile, outfile)) \
            if not "move" in args or not args["move"] else \
        (lambda infile, outfile: os.rename(infile, outfile))

    for f in files:
        place(f, action, args)


