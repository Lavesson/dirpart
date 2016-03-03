#!/usr/bin/python

import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Partition files into A-Z sub directories")

    parser.add_argument("[DIR]", help="The directory to partition")
    args = parser.parse_args()

if __name__ == "__main__":
    main()
