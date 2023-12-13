# -*- coding: utf-8 -*-

##################################################
# Function: Driver for EditImg
##################################################
# License: MIT License
##################################################
# Author: Jiucheng Zang
# Date: 2023-12-13
# Version: v1.0
# Update:
#   v1.0 at 2023-12-13
#       - Driver for EditImg
##################################################


from EditImg.editImg import EditImg

def run(EditInformation):
    editImg = EditImg(EditInformation)
    editImg.edit_saveImage()