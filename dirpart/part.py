# Author: Eric Lavesson

import os
import shutil

from os import path
import re

_DEFAULT_MISC = "!misc"
_NO_MAX_BOUNDARY = -1

def discover_files(dir):
    for f in os.listdir(dir):
        if path.isfile(path.join(dir, f)):
            yield f

def _reasonable_subdir(base_dir, base_subdir, maxitems):
    full_path = path.join(base_dir, base_subdir)

    # Unused? No worries
    if not path.isdir(full_path):
        return True

    # Unbounded? Completely fine
    if maxitems == _NO_MAX_BOUNDARY:
        return True

    # Not full? Yay for subdir
    if len(list(discover_files(full_path))) < maxitems:
        return True

    # Can't use this as a subdir
    return False

def _decide_subdir(base_dir, base_subdir, maxitems):
    full_path = path.join(base_dir, base_subdir)

    if _reasonable_subdir(base_dir, base_subdir, maxitems):
        return base_subdir

    current = 0

    while True:
        current = current + 1
        new_subdir = base_subdir + str(current)

        if _reasonable_subdir(base_dir, new_subdir, maxitems):
            return new_subdir

def place(fname, action, args):
    outdir = args["outdir"]
    indir = args["indir"]

    sdir_name = fname[:1].upper()
    sdir_name = sdir_name if not \
        re.match("^\.", sdir_name) else args["special"]
    sdir_name = _decide_subdir(
        outdir, sdir_name, int(args["maxfiles"]))

    if not path.exists(outdir):
        os.makedirs(outdir)

    full_path = path.join(outdir, sdir_name)

    if not path.exists(full_path):
        os.makedirs(full_path)

    action(path.join(indir, fname), path.join(full_path, fname))

def part_files(**args):
    if not "special" in args or not args["special"]:
        args["special"] = _DEFAULT_MISC

    if not "maxfiles" in args:
        args["maxfiles"] = _NO_MAX_BOUNDARY

    files = filter(
        lambda f: re.match(args["pattern"], f),
        discover_files(args["indir"]))

    action = \
        (lambda infile, outfile: shutil.copy2(infile, outfile)) \
            if not "move" in args or not args["move"] else \
        (lambda infile, outfile: os.rename(infile, outfile))

    for f in sorted(files):
        place(f, action, args)


