# -*- coding: utf-8 -*-

##################################################
# Function: Edit Image Class 
##################################################
# License: MIT License
##################################################
# Author: Jiucheng Zang
# Date: 2023-12-13
# Version: v1.0
# Update:
#   v1.0 at 2023-12-13
#       - Edit Image Class
##################################################


from settings import defalut_color

class EditInformation:
    def __init__(self):
        self.text = "Refreshing..."
        self.color = defalut_color
        self.font_size = 30
        self.x_value = 0
        self.y_value = 0
        self.editImgStatus = False
