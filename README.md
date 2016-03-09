## What's this?

Just a small set of python files to copy/move files into named subdirs
released under the zlib/png license. I initially created this one solely
because I needed to grab a bunch of NES roms for my Everdrive n8 and
move them into subfolders 1-8 and A-Z.

dirpart is released under the zlib/png license. Basically, you can use
this software in any way you see fit, including commercial applications.
If you use it as part of something larger, a mention would be
appreciated (but not necessary)

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

    $ dirpart . -o out/ --max=254      # Max 254 files per directory
                                       # Everything else goes into consecutive
                                       # folders (such as A, A1, A2 etc.)

## Installation

* Clone/download/whatever and make sure Python 2.7 is installed
* On Linux/UNIX, either use the command directly, or symlink:

        $ ln -s /path/to/dirpart.py /usr/bin/dirpart

* On Windows, either use the command directly, or make sure dirpart.py
  is in your path

## Running tests

To run the tests, from the root of the repository:

    $ python -m t.test_dirpart

