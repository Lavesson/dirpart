#!/usr/bin/python

# Author: Eric Lavesson
#
# I created this script solely to move a bunch of
# NES roms into folders A-Z in order to be able to
# play them on my Everdrive n8. No problems using
# this to partition any set of files into A-Z dirs
# though

import argparse
import os
from os import path

from dirpart import part

def main():
    parser = argparse.ArgumentParser(
        prog="dirpart",
        description="Partition files into A-Z sub directories")

    parser.add_argument(
        "dir", metavar="[in]",
        help="The directory to partition")
    parser.add_argument(
        "-o", "--out", metavar="[out]",
        help="Output dir. Defaults to current folder")
    parser.add_argument(
        "-m", "--move", action="store_true",
        help="Move files instead of copying")
    parser.add_argument(
        "-e", "--regexp", metavar="[pattern]",
        help="Apply to files matching the regex only")
    parser.add_argument(
        "-s", "--special", metavar="[folder]",
        help="Use a special folder to put files starting with" \
             "one or more dots. Defaults to '!misc'")

    args = parser.parse_args()

    if not path.isdir(args.dir):
        print("'{}' is not a valid directory".format(args.dir))
        return 1

    output = args.out if args.out else os.getcwd()

    return part.part_files(
        indir   = args.dir or ".",
        outdir  = output or ".",
        move    = args.move or False,
        pattern = args.regexp or "",
        special = args.special or "")

if __name__ == "__main__":
    main()

