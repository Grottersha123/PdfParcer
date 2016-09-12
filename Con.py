from __future__ import print_function
import os, sys
from PIL import Image

def convert(path,form):
   a = os.listdir(path)
   for i in a:
        if i.endswith('.jpg') or i.endswith('.png'):
            out = i.replace('.jpg',form)
            #out = i.replace('.png',form)
        Image.open(path+i).save(path+out)
        os.remove(path+i)
   #subprocess.check_output(path,)
