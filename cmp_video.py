import cv2
import os   

######              NOTE       ############
# this file is not working properly
######                          ###########


# resizing all frames
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim)

def cmp( video , num):


    # getting video and then processing it and saving in filename_ouput.mp4
    cap = cv2.VideoCapture(video)
    width  = (cap.get(3) * int(num))/ 100
    height = (cap.get(4) * int(num))/ 100
    # fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    out_video = cv2.VideoWriter('/home/ninfateni/Desktop/label/img/Compressed_'+video,0x7634706d, 20.0, (int(width), int(height)),True)
    while(cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                frameX = rescale_frame(frame,int(num))
                out_video.write(frameX) 
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
    cap.release()
    cv2.destroyAllWindows()




if __name__ == "__main__" :
    dc = ['/media/ninfateni/BCA8-ADD8/DCIM/173_0101' , '/media/ninfateni/BCA8-ADD8/DCIM/172___01' , '/media/ninfateni/BCA8-ADD8/DCIM/174_0804']
    for dir in dc :   
        os.chdir(dir)
        files = os.listdir()
        # 3. Extract all of the images:
        videos = [file for file in files if file.endswith(('MP4', ))]
        # 4. Loop over every image:
        for video in videos:
            cmp( video , 60)