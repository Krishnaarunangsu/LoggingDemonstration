import logging
import random
import os


class MyFileHandler(logging.FileHandler):
    def __init__(self,path,fileName,mode):
        r = random.randint(1,100000)
        path = path+"/log_"+str(r)
        print(path)
        os.mkdir(path)
        super(MyFileHandler,self).__init__(path+"/"+fileName,mode)
