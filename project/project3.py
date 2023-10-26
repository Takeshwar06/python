from cv2 import *

cam = VideoCapture(cam_port) 

result, image = cam.read() 

if result:
    imshow("GeeksForGeeks", image)

    imwrite("GeeksForGeeks.png", image) 

    waitKey(0) 
    destroyWindow("GeeksForGeeks") 

else: 

    print("No image detected. ")