import cv2
import os

Source = 'E:\MedicalDataset'
Destination = 'D:\data_resized'
def resizedVideos(Source , Destination):
    for File in os.listdir(Source):
      Path2 = os.path.join(Source, File)
      Destination2 = os.path.join(Destination, File)
      print(File)
      for Video in os.listdir(Path2):
         #print(Video)
         Path3 = os.path.join(Path2,Video)
         Destination3=os.path.join(Destination2,Video)
         #print(Path3)
         #print(Destination3)
         Resized(Path3,Destination3)
def Resized(path1,path2):
    cap = cv2.VideoCapture(path1)
    out = cv2.VideoWriter(path2,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (400,400))
    i = 0
    while(True):
    # Capture frame-by-frame
       ret, frame = cap.read()

       if ret==False:
          break

       frame = cv2.resize(frame,(400, 400))
       #print(frame)
       #Display the resulting frame
       out.write(frame)
       #When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
resizedVideos(Source , Destination)