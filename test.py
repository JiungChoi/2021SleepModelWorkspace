import facetracker_custom as fc
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

jiung = "jiung"
frameCnt = 0
landmarks = []
toMotionNum = 400
fromMotionNum = 1


model = load_model("output_02.h5")
model.summary() # model Info

frameCnt = 0
for points in fc.run(visualize=1, max_threads=4, capture=0):
    frameCnt += 1
    if (frameCnt//2 == 1):
        frameCnt = 0
        landmarks.append(points)
        if len(landmarks) == 30:
            h = model.predict(landmarks)
            print(f"Sleep [{(h[0][1]*100)//1}%]") if h.argmax() == 1 else print(f"NO Sleep [{(h[0][0])*100//1}%]")
            
