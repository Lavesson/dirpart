#!/usr/bin/python

# Author: Eric Lavesson
#
# I created this script solely to move a bunch of
# NES roms into folders A-Z in order to be able to
# play them on my Everdrive n8. No problems using
# this to partition any set of files into A-Z dirs
# though

import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Partition files into A-Z sub directories")

    parser.add_argument("[DIR]", help="The directory to partition")
    args = parser.parse_args()

if __name__ == "__main__":
    main()
