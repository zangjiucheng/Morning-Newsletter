# -*- coding: utf-8 -*-

##################################################
# Function: Main Function
##################################################
# License: MIT License
##################################################
# Author: Jiucheng Zang
# Date: 2023-12-13
# Version: v1.0
# Update:
#   v1.0 at 2023-12-13
#       - Main Function
##################################################

import sys
from settings import abs_path

sys.path.append(abs_path)

if __name__ == '__main__':
    from frontWeb import app
    app()
