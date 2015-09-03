import cPickle as pickle
import pdb
import os
class mvmt:
    def __init__(self, file_loc, sbj_id, day_num):
        self.file_loc = file_loc
        self.sbj_id = sbj_id
        self.day_num = day_num
        self.cur_file_num = 0
        #pdb.set_trace()
        self.cur_mvmt = pickle.load(open(self.file_loc + "\\" + sbj_id + "_" + str(day_num) \
                                + "_" + format(self.cur_file_num, '04') + ".p", 'rb'))
        
        self.cur_mvmt_len = len(self.cur_mvmt)
        self.cur_frame = 0
        self.cur_file_num += 1
        
        
        
    def load_new_file(self):
        self.cur_mvmt = pickle.load(open(self.file_loc + "\\" + self.sbj_id + "_" + str(self.day_num) \
                                + "_" + format(self.cur_file_num, '04') + ".p", 'rb'))
        self.cur_mvmt_len = len(self.cur_mvmt)
        self.cur_frame = 0
        self.cur_file_num += 1

    def has_next(self):
        if self.cur_frame >= self.cur_mvmt_len:
            return os.path.isfile(self.file_loc + "\\" + self.sbj_id + "_" + str(self.day_num) \
                                + "_" + format(self.cur_file_num , '04') + ".p")
        else: return True
    
    def next(self):
        if self.cur_frame >= self.cur_mvmt_len:
            self.load_new_file()
        mvmt_val = self.cur_mvmt[self.cur_frame]
        self.cur_frame += 1
        
        return mvmt_val

    def rewind(self):
        self.cur_mvmt = None
        self.cur_mvmt_len = 0
        self.cur_file_num = 0
        load_new_file()
        self.cur_frame = 0
        