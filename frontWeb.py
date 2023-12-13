# -*- coding: utf-8 -*-

##################################################
# Function: Streamlit Front End
##################################################
# License: MIT License
##################################################
# Author: Jiucheng Zang
# Date: 2023-12-13
# Version: v1.0
# Update:
#   v1.0 at 2023-12-13
#       - Streamlit Front End
##################################################

from settings import api_key,abs_path,defalut_color,defalut_font_size,default_x_value,default_y_value
import streamlit as st 
from time import sleep
from collectInfo import Information
from EditImg import driver
from EditImg.informationClass import EditInformation

def app():
    editInformation = EditInformation()
    editInformation.text = Information.run(api_key)
    if st.button("Update Information? *Information won't be saved*"):
        editInformation.text = Information.run(api_key)
    editInformation.text = st.text_area('DataInput', editInformation.text,height=250)
    editInformation.x_value = st.slider('x_value', 0, 100, default_x_value)
    editInformation.y_value = st.slider('y_value', 0, 100, default_y_value)
    editInformation.font_size = st.slider('font_size', 0, 130, defalut_font_size)
    editInformation.color = st.color_picker('Pick A Color', defalut_color)
    on = st.toggle('Change Background Image?', True)
    if on: #Fix later need constant update
        editInformation.editImgStatus = True
    else:
        editInformation.editImgStatus = False
    driver.run(editInformation)
    sleep(3)
    st.image(abs_path+'output.png', caption='Privew Image')