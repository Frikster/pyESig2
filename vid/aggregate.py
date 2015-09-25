import cPickle as pickle
import numpy as np
import os
import edflib._edflib as edflib
import pdb
import matplotlib.pyplot as plt
from pyESig.vid.mvmt_class import mvmt
from pyESig.vid.misc_funcs import has_video

sbj_id = "e70923c4"
day = 5
sr=30
input_file_loc = "E:\\sound\\"
#output_file_loc = "C:\\Users\\wangnxr\\Documents\\rao_lab\\video_decode\\sound_result_agg\\"
output_file_loc = input_file_loc
has_video_array = has_video("C:\\Users\\wangnxr\\Documents\\rao_lab\\video_analysis\\disconnect_times\\" \
                            + sbj_id + "_" + str(day) + ".txt", samp_rate = sr)

total_mvmt = np.zeros(has_video_array.shape[0])
mvmt_obj = mvmt(input_file_loc, sbj_id, day)
for f in xrange(has_video_array.shape[0]):
    if has_video_array[f] == 0:
        total_mvmt[f] = -1
    else:
        if mvmt_obj.has_next():
            total_mvmt[f] = mvmt_obj.next()
        else:

            total_mvmt[f] = -1

pdb.set_trace()
pickle.dump(total_mvmt, open(output_file_loc + sbj_id + "_" + str(day) + ".p" , "wb"))
plt.plot(np.array(range(270*30*60))/(60*30.0), total_mvmt[:270*30*60])
#plt.ylim([10**11,6*10**15])
plt.xlabel("Time (Min)")
plt.ylabel("Speech sound level")
plt.show()
