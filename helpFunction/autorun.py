# -*- coding: utf-8 -*-

# Not working yet

from time import strftime, localtime, sleep
from settings import abs_path

if argus.status == False:
    while True:
        now = strftime('%H', localtime())
        # data.writeJsonData() 
        if now == "07":
            argus = Argus.Argus()
            data = Data.Data(abs_path,api_key)
            send_post(argus.status, argus.email) 
        else:
            sleep(900)
else:
    send_post(argus.status, argus.email)