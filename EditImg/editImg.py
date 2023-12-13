# -*- coding: utf-8 -*-

##################################################
# Function: Edit Image with text
##################################################
# License: MIT License
##################################################
# Author: Jiucheng Zang
# Date: 2023-12-13
# Version: v1.0
# Update:
#   v1.0 at 2023-12-13
#       - Edit Image with text
##################################################

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from settings import write_font,abs_path, output_img

import os
import random

class EditImg:
    def __init__(self,infortmationUpdate):
        self.info = infortmationUpdate
        if infortmationUpdate.editImgStatus:
            self.imgPath = abs_path+"img/"+self.radomSelect(abs_path+"img/")
        self.text = self.info.text
        self.img = Image.open(self.imgPath)
        self.width = self.info.x_value/100*self.img.size[0]
        self.height = self.info.y_value/100*self.img.size[1]
        self.font = ImageFont.truetype(abs_path+"Font/"+write_font, self.info.font_size)
        self.outputPath = abs_path+output_img
        self.text_color = self.info.color
        
    # def random_color_generator(self):
    #     r = random.randint(0, 255)
    #     g = random.randint(0, 255)
    #     b = random.randint(0, 255)
    #     return (r, g, b)
    
    def hex_to_rgb(hex):
        rgb = []
        for i in (0, 2, 4):
            decimal = int(hex[i+1:i+3], 16)
            rgb.append(decimal)
        
        return tuple(rgb)


    def radomSelect(self, imagesPath):
        pathDir = os.listdir(imagesPath)
        sample1 = random.sample(pathDir, 1)  # 随机选取picknumber数量的样本
        return sample1[0]
    
    def edit_saveImage(self):
        # print(abs_path+"Font/"+write_font)
        ImageDraw.Draw(self.img).text((self.width, self.height),self.text,self.text_color,font=self.font)
        self.img.save(self.outputPath)



