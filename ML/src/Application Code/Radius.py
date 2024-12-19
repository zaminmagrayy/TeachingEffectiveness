import cv2
import numpy as np
import math
from mtcnn.mtcnn import MTCNN
import pdb
import random
import pandas as pd
cap =cv2.VideoCapture("/home/arpita/Desktop/ArpitaData/Arpita/VideoData/ApoorvaFullDistracted.mp4")
#cap=cv2.VideoCapture(0)
delta = 10
refresh = 20
x_end = 1200
y_end = 700
counter_array=[]
text_width = 50
text_height = 10
bar_height=150
bar_width=text_width/2
END=(int(x_end-text_width),int(text_height))
START=(int(x_end-0.5*text_width),int(text_height+bar_height))

Nose=[]

a=[]
counter=0
ans_array=[]

nose_sort_new=[]
font = cv2.FONT_HERSHEY_SIMPLEX 
  
# org 
org = (900, 360) 
org_1=(1070,360)
start_att = (900, 160) 
end_att = (950, 160) 
start_notatt=(900+110, 160)
end_notatt=(1010+50,160)
  
# fontScale 
fontScale = 1
required_ans_array=[]
   
# Blue color in BGR 
color_attentive = (0, 255, 0) 
color_notattentive=(0,0,255)
  
# Line thickness of 2 px 
thickness = 2
percent_attentive=0
percent_notattentive=0
#fps = cap.get(cv2.CAP_PROP_FPS)

detector=MTCNN()
# cap =cv2.VideoCapture("Video.mp4")

#cap =cv2.VideoCapture("/home/arpita/Desktop/ArpitaData/Arpita/VideoData/ApoorvaLittleDistracted.mp4")
cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 600,400)
while(True):
  # Capture frame-by-frame
  #Nose=[]
  Nose=[(0,0)]*100 # so that if 1st frame is having 0 people and then new person comes it should work.
  matrix=[]
  ret, video_capture = cap.read()
  result = detector.detect_faces(video_capture)
  counter_attentive=0
  counter_notattentive=0
  for i in result:
    nose = i['keypoints']['nose']
    #confidence=i['keypoints']['confidence']
    bounding_box = i['box']
    cv2.rectangle(video_capture,
                   (bounding_box[0], bounding_box[1]),
                   (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),(255,255,255),
                   2)
    Nose.append(nose)
  #print(Nose)
  if counter==0:
    ideal_matrix=Nose
    ideal_matrix=np.asarray(ideal_matrix)
  if len(ideal_matrix)==0:
  	percent_notattentive=0
  #print(ideal_matrix)

   
  def distance(Nose,ideal_matrix):
    diff_x=(Nose[0]-ideal_matrix[0])**2
    diff_y=(Nose[1]-ideal_matrix[1])**2
    ans=math.sqrt(diff_x+diff_y)
    return ans


  def  mapper(Nose, ideal_matrix):
    result=[(0,0)]*len(ideal_matrix)
    for i in range(0,len(Nose)):
        min_a = 1000
        k = 0
        for j in range(0,len(ideal_matrix)):
            dist = distance(Nose[i], ideal_matrix[j])
            if min_a > dist:
                min_a= dist
                k = j
            
        result[k]=Nose[i]
    return result
  
  counter=counter+1
  counter_array.append(counter)
  #print(counter)
  nose_sort_new=[]
  matrix=[0]*len(ideal_matrix)
  matrix=np.asarray(mapper(Nose,ideal_matrix))
  diff=matrix-ideal_matrix
  ans_array=[]
  #required_ans_array=[]
  
  for a in range(0,len(diff)):
    ans=math.sqrt(((diff[a][0])**2 + (diff[a][1])**2))
    ans_array.append(ans)
    if ans >0 and ans< delta:
      cv2.circle(video_capture,(matrix[a][0],matrix[a][1]) , 25, (0,255,0), 2)
    elif ans>=delta:#delta is threshold
      counter_notattentive=counter_notattentive+1
      if matrix[a][0]!=0 and matrix[a][1]!=0:
        cv2.circle(video_capture,(matrix[a][0],matrix[a][1]) , 25, (0,0,255), 2)
  print(ans_array)
  #print(ans_array)    
  required_ans_array.append(ans_array[len(ans_array)-1])
  for o in range(0,len(required_ans_array)):
    if required_ans_array[o]>200:
        required_ans_array[o]=required_ans_array[o-1]

  #print(required_ans_array) 
  percent_notattentive=(counter_notattentive/len(ideal_matrix))*100
  percent_attentive=100-percent_notattentive
  if percent_attentive<70:
  	cv2.putText(video_capture,"ALERT!!", (10,70), font,2, (0,0,255), thickness, cv2.LINE_AA)  


  #print(percent_attentive)
  
    cv2.imshow('frame',video_capture)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
df=pd.DataFrame({'frame':counter_array,'radius':required_ans_array})
#df = pd.DataFrame({'x':x, 'y':y})
df.to_csv('FullDistractedData.csv',index=False) 
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(0)
