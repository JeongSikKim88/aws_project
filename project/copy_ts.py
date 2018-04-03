import os
import shutil
import time
import fnmatch

walk_dir = "/root/ess_exec/objs/nginx/html/app01"
work_space = "/home/centos/backup"
ts_folder = "/home/centos/project"
count = 0

ipcam_dir = ("/home/centos/vod/ipcam1/", "/home/centos/vod/ipcam2/", "/home/centos/vod/ipcam3/")
heat_dir = ("/home/centos/vod/heat1/", "/home/centos/vod/heat2/", "/home/centos/vod/heat3/")
ricoh_dir = ("/home/centos/vod/ricoh1/", "/home/centos/vod/ricoh2/", "/home/centos/vod/ricoh3/")
# ipcam1_dir = "/home/centos/vod/ipcam1/"
# ipcam2_dir = "/home/centos/vod/ipcam2/"
# ipcam3_dir = "/home/centos/vod/ipcam3/"
# heat1_dir = "/home/centos/vod/heat1/"
# heat2_dir = "/home/centos/vod/heat2/"
# heat3_dir = "/home/centos/vod/heat3/"
# ricoh1_dir = "/home/centos/vod/ricoh1/"
# ricoh2_dir = "/home/centos/vod/ricoh2/"
# ricoh3_dir = "/home/centos/vod/ricoh3/"

pattern_ipcam = ('ipcam1*', 'ipcam2*', 'ipcam3*')
pattern_heat = ('heat1*', 'heat2*', 'heat3*')
pattern_ricoh = ('ricoh1*', 'ricoh2*', 'ricoh3*')
# pattern_ipcam2 = 'ipcam2*'
# pattern_ipcam3 = 'ipcam3*'
# # pattern_heat1 = 'heat1*'
# # pattern_heat2 = 'heat2*'
# pattern_heat3 = 'heat3*'
# pattern_ricoh1 = 'ricoh1*'
# pattern_ricoh2 = 'ricoh2*'
# pattern_ricoh3 = 'ricoh3*'

for root, subdir, files in os.walk(walk_dir):
    for file in files:
        if (file.split(".")[-1].lower() == 'ts'):
            if (fnmatch.fnmatch(file, pattern_ipcam[0])):
                filePath = os.path.join(root, file)
                try:
                    created_time = time.ctime(os.path.getctime(filePath))
                    shutil.copy(filePath, ipcam_dir[0] + created_time + ".ts")
                except:
                    continue
                count = count + 1
            elif (fnmatch.fnmatch(file, pattern_ipcam[1])):
                filePath = os.path.join(root, file)
                try:
                    created_time = time.ctime(os.path.getctime(filePath))
                    shutil.copy(filePath, ipcam_dir[1] + created_time + ".ts")
                except:
                    continue
                count = count + 1
            elif (fnmatch.fnmatch(file, pattern_ipcam[2])):
                filePath = os.path.join(root, file)
                try:
                    created_time = time.ctime(os.path.getctime(filePath))
                    shutil.copy(filePath, ipcam_dir[2] + created_time + ".ts")
                except:
                    continue
                count = count + 1
            elif (fnmatch.fnmatch(file, pattern_heat[0])):
                filePath = os.path.join(root, file)
                try:
                    created_time = time.ctime(os.path.getctime(filePath))
                    shutil.copy(filePath, heat_dir[0] + created_time + ".ts")
                except:
                    continue
                count = count + 1
            elif (fnmatch.fnmatch(file, pattern_heat[1])):
                filePath = os.path.join(root, file)
                try:
                    created_time = time.ctime(os.path.getctime(filePath))
                    shutil.copy(filePath, heat_dir[1] + created_time + ".ts")
                except:
                    continue
                count = count + 1
            elif (fnmatch.fnmatch(file, pattern_heat[2])):
                filePath = os.path.join(root, file)
                try:
                    created_time = time.ctime(os.path.getctime(filePath))
                    shutil.copy(filePath, heat_dir[2] + created_time + ".ts")
                except:
                    continue
                count = count + 1
            elif (fnmatch.fnmatch(file, pattern_ricoh[0])):
                filePath = os.path.join(root, file)
                try:
                    created_time = time.ctime(os.path.getctime(filePath))
                    shutil.copy(filePath, ricoh_dir[0] + created_time + ".ts")
                except:
                    continue
                count = count + 1
            elif (fnmatch.fnmatch(file, pattern_ricoh[1])):
                filePath = os.path.join(root, file)
                try:
                    created_time = time.ctime(os.path.getctime(filePath))
                    shutil.copy(filePath, ricoh_dir[1] + created_time + ".ts")
                except:
                    continue
                count = count + 1
            elif (fnmatch.fnmatch(file, pattern_ricoh[2])):
                filePath = os.path.join(root, file)
                try:
                    created_time = time.ctime(os.path.getctime(filePath))
                    shutil.copy(filePath, ricoh_dir[2] + created_time + ".ts")
                except:
                    continue
                count = count + 1

print ("Copy file to work_space: ", count)
