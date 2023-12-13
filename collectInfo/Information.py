# -*- coding: utf-8 -*-

##################################################
# Function: Test for collectInfo
##################################################
# License: MIT License
##################################################
# Author: Jiucheng Zang
# Date: 2023-12-13
# Version: v1.0
# Update:
#   v1.0 at 2023-12-13
#       - Test for collectInfo
##################################################

import collectInfo.Argus as Argus
import collectInfo.Data as Data
from settings import abs_path

def run(api_key):
    global data, argus
    argus = Argus.Argus()
    data = Data.Data(abs_path,api_key)
    return data.mail_data

def print_data():
    print(data.mail_data)

# if __name__ == "__main__":
#     print(run())