from PIL import Image
import PIL
import os
import glob


def compress_images(directory, quality=60):
    # 1. If there is a directory then change into it, else perform the next operations inside of the 
    # current working directory:
    if directory:
        os.chdir(directory)

    # 2. Extract all of the .png and .jpeg files:
    files = os.listdir()

    # 3. Extract all of the images:
    images = [file for file in files if file.endswith(('JPG', 'png'))]
    # 4. Loop over every image:
    for image in images:

        # 5. Open every image:
        img = Image.open(image)

        # 5. Compress every image and save it with a new name:
        img.save("/home/ninfateni/Desktop/label/img/Compressed_"+image, optimize=True, quality=quality)

dc = ['/media/ninfateni/BCA8-ADD8/DCIM/173_0101' , '/media/ninfateni/BCA8-ADD8/DCIM/172___01' , '/media/ninfateni/BCA8-ADD8/DCIM/174_0804']
for dir in dc :
    compress_images(directory=dir)