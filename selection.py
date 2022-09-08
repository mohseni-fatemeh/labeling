import shutil
import os

original_path = "/home/ninfateni/Desktop/label/img/"
destination_path = "/home/ninfateni/Desktop/label/label_img/"


os.chdir(original_path)
files = os.listdir()
txts = [file for file in files if file.endswith(('txt',))]
for txt in txts :
    ls = str(txt.split('.')[0])+'.jpg'
# copy jpg
    if ls == "classes.jpg" :
        pass
    else:
        source  = original_path+ls
        destination = destination_path+ls

        dest = shutil.copyfile(source, destination)
# copy txt
    source = original_path+txt
    destination = destination_path+txt

    dest = shutil.copyfile(source ,destination)