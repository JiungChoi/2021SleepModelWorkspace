import facetracker_custom as fc
import pandas as pd
import csv
jiung = "jiung"
frameCnt = 0
landmarks = []
toMotionNum = 400
fromMotionNum = 1

for points in fc.run(visualize=1, max_threads=4, capture=0):
    
    frameCnt += 1
    if (frameCnt//2 == 1):
        frameCnt = 0
        landmarks.append(points)
        if len(landmarks) == 30:
            print(f"{fromMotionNum}")
            df = pd.DataFrame(landmarks)
            df.to_csv(f"{fromMotionNum}.csv", header =None, index=None)
            
            fromMotionNum+=1
            if fromMotionNum> toMotionNum : break
            frameCnt = 0
            landmarks= []


'''
motion = []
motion_csv = csv.reader(open("wldnd.csv", "r", encoding = "UTF-8"))
for frame_csv in motion_csv:
    motion.append(frame_csv)

for frame in range(len(motion)): # 0~30
    for points in range(len(motion[0])): # 0~68
        motion[frame][points] = [float(motion[frame][points].strip("[]").split(",")[0]),float(motion[frame][points].strip("[]").split(",")[1])]
'''
'''
'''