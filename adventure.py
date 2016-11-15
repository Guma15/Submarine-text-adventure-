#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is the client for a text adventure game.
"""

import sys
import os
from datetime import datetime
import getopt
import gameMain

PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Guma15"
EMAIL = "Email"
VERSION = "1.0.0"
USAGE = """{program} - Print my name. By {author} ({email}), version {version}.

Usage:
  {program} [options]

Options:
  -h --help            Display this help message.
  -i --info            Describes the general idea of the game.
  -v --version         Print version of the program
  -a --about           Displays information of the author for the program.
  -c --cheat           Describes the shortest route to finish the game.

  start                Starts the game.
""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)

MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)

INFO = """
    The game is a short text adventure that takes place on a submarine in the
    pacific ocean researching a strange material found around the Marianna Trench.
    You are the first-mate at the submarine and have been asked by the captain to
    go get the research results from a research sample at the submarine lab. However
    the submarine have been facing some technical problems that have made the trip
    to the lab not as straight forward as first thought...

    The initial idea for the game is to solve different puzzles in seven of the rooms on
    the submarine to eventually gain access to the lab and deliver the research results
    to the captain.
"""

ABOUT = """{program} - Print my name. By {author} ({email}), version {version}.

    I am a system science program student. I am currently trying to expand my
    programming knowledge as well as my webdevelopment skills to be used for a
    future career or as a hobby.

    The game was created for a Python school project at Blekinge University of
    Technology. The project topic was to create a short text adventure with a
    few puzzles.

    The setting of the game was inspired by an old game idea that never came to
    fruition. I might one day create a full game when I feel that I got the time
    and knowledge to do so.

""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)

CHEAT = """Shortest route to clear the game is to:
west > west > use control panel > 1, 1, 2, 3 > west > east > open hatch >
north > use keypad > 2131 > north > use computer > 1, 1, 3 > south > south >
east > north > Finished!
"""

#
# Global default settings affecting behaviour of script in several places
#

EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2

def printUsage(exitStatus):
    """
    Print usage information about the script and exit.
    """
    print(USAGE)
    sys.exit(exitStatus)

def printInfo():
    """
    Print information about the game and exit.
    """
    print(INFO)
    sys.exit(EXIT_SUCCESS)

def printVersion():
    """
    Print version information and exit.
    """
    print(MSG_VERSION)
    sys.exit(EXIT_SUCCESS)

def printAbout():
    """
    Print a short description about the author.
    """
    print(ABOUT)
    sys.exit(EXIT_SUCCESS)

def printCheat(derp=None):
    """
    Print the shorest route to finish the game.
    """
    print(CHEAT)
    print(derp)
    sys.exit(EXIT_SUCCESS)

def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """

    # Switch through all options
    try:

        opts, args = getopt.getopt(sys.argv[1:], "hivac:", [
            "help",
            "info",
            "version",
            "about",
            "cheat=",
            "start"])

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                printUsage(EXIT_SUCCESS)

            elif opt in ("-i", "--info"):
                printInfo()

            elif opt in ("-v", "--version"):
                printVersion()

            elif opt in ("-a", "--about"):
                printAbout()

            elif opt in ("-c", "--cheat"):
                output = arg
                printCheat(output)

            else:
                assert False, "Unhandled option"

        # All commands
        if args[0] == "start":
            print("Go")
            gameMain.gameStart()


    except Exception as err:
        print(err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        #traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)

def main():
    """
    Main function to carry out the work.
    """
    startTime = datetime.now()

    parseOptions()

    timediff = datetime.now()-startTime
    sys.stderr.write("Script executed in {}.{} seconds\n".format(timediff.seconds, timediff.microseconds))

    sys.exit(EXIT_SUCCESS)



if __name__ == "__main__":
    main()
