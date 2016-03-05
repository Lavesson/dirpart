## What's this?

Just a small set of python files to copy/move files into named subdirs.
I initially created this one solely because I needed to grab a bunch
of NES roms for my Everdrive n8.

## How does it work?

    $ ls
    a_file  a_file_2  b_file  x_file
    $ dirpart . -o out/
    $ ls out/
    A B X
    $ ls out/A
    a_file  a_file_2

... And so on

## Common uses

    $ dirpart . -o out/                # Part files into subdirs in out/
                                       # by copying the files

    $ dirpart . -o out/ --move         # Same deal, but moving the files
                                       # instead of copying

    $ dirpart . -o out/ --regexp='...' # Only apply to files matching
                                       # the given regular expression

## Installation

* Clone/download/whatever and make sure Python 2.7 is installed
* Either use the command directly, or symlink:

    $ ln -s /path/to/dirpart.py /usr/bin/dirpart

## Running tests

To run the tests, from the root of the repository:

    $ python -m t/test_dirpart

