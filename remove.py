import os

original_path = "/home/ninfateni/Desktop/label/img/"

os.chdir(original_path)
files = os.listdir()
txts = [file for file in files if file.endswith(('txt',))]
for txt in txts :
    os.remove(txt)