#creates a debian package for the current version of the program

import os
from os import system
from os import remove
from os import path
from shutil import copyfile
from shutil import rmtree
from shutil import move
from platform import system as platform
from sys import exit
from sys import argv
from sys import version_info
from sys import executable