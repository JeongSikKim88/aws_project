#!/usr/local/opt/python/bin/python2.7
# Required ffmpeg

import os
import shutil
import time

walk_dir = "/root/ess_exec/objs/nginx/html/app01"
work_space = "/home/centos/backup"
ts_folder = "/home/centos/project"
count = 0



for root, subdir, files in os.walk(walk_dir):
    for file in files:
        if (file.split(".")[-1].lower() == 'ts'):
            filePath = os.path.join(root, file)
            created_time = time.ctime(os.path.getctime(filePath))
            shutil.copy2(filePath, created_time + ".ts")
            count = count + 1
print "Copy file to work_space: ", count

# def Econding(work_space):
# for root, subdir, files in os.walk(ts_folder):
#     for file in files:
#         if (file.split(".")[-1].lower() == 'ts'):
#             filePath = os.path.join(root, file)
#             mp4FilePath = os.path.join(root, os.path.splitext(file)[0] + ".mp4")
#             if os.path.isfile(mp4FilePath):
#                 continue
#             os.system("ffmpeg -i " + "\"" + filePath + "\"" + " \"" + mp4FilePath + "\"")
#             count = count + 1
#

# def Encoding(work_space):
#     pass



print "Done the total number of file was be converted: ", count
