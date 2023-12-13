# -*- coding: utf-8 -*-

# Not working yet

import getopt
import sys

class Argus:
    def __init__(self):
        self.email = ""
        self.status = False
        self.getArgv()

    def getArgv(self):
        try:
            opts, arg = getopt.getopt(sys.argv[1:], "ye:", ["yes", "email="])
        except getopt.GetoptError:
            print('Error: morning_post.py -y -e <email_adress>')
            print('   or: morning_post.py --yes --email=<email_adress>')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-y", "--yes"):
                self.status = True
            elif opt in ("-e", "--email"):
                self.email = arg