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

def discover_files(dir):
    for f in os.listdir(dir):
        if path.isfile(os.path.join(dir, f)):
            yield f

def part_files(dir):
    files = discover_files(dir)

    for f in files:
        print(f)

def main():
    parser = argparse.ArgumentParser(
        description="Partition files into A-Z sub directories")

    parser.add_argument("dir", metavar="[DIR]", help="The directory to partition")
    args = parser.parse_args()

    if not path.isdir(args.dir):
        print("'{}' is not a valid directory".format(args.dir))
        return 1

    return part_files(args.dir)

if __name__ == "__main__":
    main()

