import subprocess as sp
import numpy as np
import matplotlib.pyplot as plt
import pdb
from pyESig.vid.face_blur import face_blur
import pickle
from pyESig.vid.my_video_capture import my_video_capture
import cv2
import os

sbj_id = "a86a4375"
sbj_id = "ea430431"
day = 2
samp_rate = 8000
num_secs = 120
vid_num = 78
vid_num = 27
vid_num_pad = str(vid_num).zfill(4)

mvmt_file_loc = "D:\\NancyStudyData\\ecog\\mvmt\\" + sbj_id + "\\" + sbj_id \
                 + "_" + str(day) + "_" + vid_num_pad + ".p"
mvmt_file_loc = "D:\\NancyStudyData\\eeg\\mvmt\\" + sbj_id + "\\" + sbj_id \
                 + "_" + str(day) + "_" + vid_num_pad + ".p"
video_file_loc = "D:\\NancyStudyData\\ecog\\raw\\" + sbj_id + "\\" + sbj_id \
                 + "_" + str(day) + "\\"
video_file_loc = "D:\\NancyStudyData\\eeg\\raw\\" + sbj_id + "\\" + sbj_id \
                 + "_" + str(day) + "\\"
output_file_loc = video_file_loc

#face_blur(video_file_loc + "Timm~Katrina_497a1ff8-9b6f-4868-bd2d-752c6b86e192_0078.avi")
#face_blur(video_file_loc + sbj_id + "_" + str(day) + "_0027.avi")

mvmt = pickle.load(open(mvmt_file_loc, "rb"))
#pdb.set_trace()
##for m in range(0,mvmt.shape[0], 30):
##    if np.where(mvmt[m:m+30] > 1.1)[0].shape[0] > 5:
##        mvmt[m:m+30] = 1
##    if np.where(mvmt[m:m+30] > 1.2)[0].shape[0] > 5:
##        mvmt[m:m+30] = 2
##    if np.where(mvmt[m:m+30] > 1.1)[0].shape[0] < 5:
##        mvmt[m:m+30] = 0
mvmt2 = np.zeros(mvmt.shape[0])
for m in range(0,mvmt.shape[0]-30):
    mvmt2[m] = np.mean(mvmt[np.where(mvmt[m:m+30]>0)[0]+m])


mvmt2 = (mvmt2 - np.mean(mvmt2))/np.std(mvmt2)

for m in range(0,mvmt.shape[0]):
    if mvmt2[m]>3:
        mvmt2[m]/=3
    if mvmt2[m]<0:
        mvmt2[m]=0


cam = my_video_capture(video_file_loc + \
    "Timm~Katrina_497a1ff8-9b6f-4868-bd2d-752c6b86e192_0078_2.avi", 30)
cam = my_video_capture(video_file_loc + \
    "Lori~Grigor_a2f52bb6-db8b-4f4f-9763-344db14ef2ce_0027_2.avi", 30)
frame_cnt = 1

while cam.has_next():
    plt.figure(figsize=(6.4, 0.5), dpi = 10)
    plt.plot(range(mvmt2.shape[0]), mvmt2, mew=0.1)

    plt.ylim([0,4])
    plt.axis('off')
    plt.text(0.1,1,"Movement\n levels\n", ha='right', \
                 va = 'center', fontsize=10)
    marker_on = frame_cnt-15
    plt.plot(marker_on, 2, marker = '|', mew=2, markersize=100)
    plt.savefig(output_file_loc + "tmp.png", dpi = 100)
    

    img = cam.read()
    graph = cv2.imread(output_file_loc + "tmp.png")
    img[480-50:480, 0:640] = graph
    cam.write(img, frame_cnt)
    frame_cnt += 1
    print frame_cnt
    plt.close('all')
fileName, fileExt = os.path.splitext(video_file_loc + \
            "Timm~Katrina_497a1ff8-9b6f-4868-bd2d-752c6b86e192_0078.avi")
fileName, fileExt = os.path.splitext(video_file_loc + \
            "Lori~Grigor_a2f52bb6-db8b-4f4f-9763-344db14ef2ce_0027.avi")
cam.new_vid(fileName + fileExt)

cv2.destroyAllWindows()
    
    

