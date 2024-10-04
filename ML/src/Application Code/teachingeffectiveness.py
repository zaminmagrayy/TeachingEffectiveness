import cv2
import numpy as np
import math
from mtcnn.mtcnn import MTCNN
import pdb
import random

delta = 10
refresh = 20

detector=MTCNN()
cap =cv2.VideoCapture("Video.mp4")

cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 600,400)

x_end = 1200
y_end = 700

text_width = 50
text_height = 10
bar_height=150
bar_width=text_width/2
END=(int(x_end-text_width),int(text_height))
START=(int(x_end-0.5*text_width),int(text_height+bar_height))

Nose=[]

a=[]
counter=0

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
   
# Blue color in BGR 
color_attentive = (0, 255, 0) 
color_notattentive=(0,0,255)
  
# Line thickness of 2 px 
thickness = 2
percent_attentive=0
percent_notattentive=0


while(True):
  # Capture frame-by-frame
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
   
  if counter==0:
    ideal_matrix=Nose
    ideal_matrix=np.asarray(ideal_matrix)
  if len(ideal_matrix)==0:
  	percent_notattentive=0

    
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
  #print(counter)
  nose_sort_new=[]
  matrix=[0]*len(ideal_matrix)
  matrix=np.asarray(mapper(Nose,ideal_matrix))
  diff=matrix-ideal_matrix
  for a in range(0,len( diff)):
    ans=math.sqrt(((diff[a][0])**2 + (diff[a][1])**2))
    if ans >0 and ans< delta :
      cv2.circle(video_capture,(matrix[a][0],matrix[a][1]) , 25, (0,255,0), 2)
    elif ans>=delta:#delta is threshold
      counter_notattentive=counter_notattentive+1
      cv2.circle(video_capture,(matrix[a][0],matrix[a][1]) , 25, (0,0,255), 2)

  percent_notattentive=(counter_notattentive/len(ideal_matrix))*100
  percent_attentive=100-percent_notattentive
  if percent_attentive<70:
  	cv2.putText(video_capture,"ALERT!!", (10,70), font,2, (0,0,255), thickness, cv2.LINE_AA)  


  print(percent_attentive)
  ACTUAL_END_ATTENTIVE=(int((START[0]-END[0])*percent_attentive/100),int((START[1]-END[1])*percent_attentive/100))
  ACTUAl_END_NOTATTENTIVE=(int((START[0]-END[0])*percent_notattentive/100),int((START[1]-END[1])*percent_notattentive/100))
  #start_att = (int(start_att[0]), int(end_att[1] - percent_notattentive*10))
  #start_notatt=(int(start_notatt[0]),int(end_notatt[1])-percent_notattentive*10)
  def bargraph_function():
  	
  	cv2.rectangle(video_capture,(1118,0),(1278,235),(255,2555,255),-1)
  	cv2.putText(video_capture, " 0_", (START[0]-40,START[1]), font,0.5, (0,0,0), 1, cv2.LINE_AA)
  	cv2.putText(video_capture, " 50_", (START[0]-40,START[1]-50), font,0.5, (0,0,0), 1, cv2.LINE_AA)
  	cv2.putText(video_capture, "100_", (START[0]-40,START[1]-100), font,0.5, (0,0,0), 1, cv2.LINE_AA)
  	cv2.rectangle(video_capture,START,(START[0]+50,int(START[1]-100)),(255,255,255),2)
  	cv2.rectangle(video_capture,START,(START[0]+50,int(START[1]-percent_attentive)),(0,255,0),-1)
  	cv2.rectangle(video_capture,START,(START[0]+100,int(START[1]-100)),(255,255,255),2)
  	cv2.rectangle(video_capture,(START[0]+55, START[1]),(START[0]+100,int(START[1]-percent_notattentive)),(0,0,255),-1)
  	#cv2.rectangle(video_capture,(1118,0),(1278,235),(255,2555,255),-1)
  	cv2.putText(video_capture,"Attentive",(1177,200),font,0.5,(0,255,0),1,cv2.LINE_AA)
  	cv2.putText(video_capture,"NotAttentive",(1177,225),font,0.5,(0,0,255),1,cv2.LINE_AA)

  	
  bargraph_function()
  # cv2.putText(video_capture, str(percent_attentive), (900,200), font,fontScale, (0,255,0), thickness, cv2.LINE_AA)  
  # cv2.putText(video_capture,str(percent_notattentive),(1070,300), font,fontScale,(0,0,255), thickness, cv2.LINE_AA) 
  if counter%refresh == 0:
    ideal_matrix = Nose
  
  cv2.imshow('frame',video_capture)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(0)
