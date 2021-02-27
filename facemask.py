# -*- coding: utf-8 -*-
"""facemask.ipynb



import cv2
from mtcnn import MTCNN as mc
mask = mc()
video_capture = cv2.VideoCapture(0)
 
while (True):
    ret, frame = video_capture.read()
    frame = cv2.resize(frame, (600, 400))
    boxes = detector.detect_faces(frame)
    if boxes:
 
        box = boxes[0]['box']
        conf = boxes[0]['confidence']
        x, y, w, h = box[0], box[1], box[2], box[3]
 
        if conf > 0.5:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)
 
    cv2.imshow("Frame", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
 


video_capture.release()
cv2.destroyAllWindows()
