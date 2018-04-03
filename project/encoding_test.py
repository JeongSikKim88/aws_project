import os
import boto3

# from multiprocessing

# walk_dir = "/root/ess_exec/objs/nginx/html/app01"
# work_space = "/home/centos/backup"
ipcam_ts_folder = ("/home/centos/vod/ipcam1/", "/home/centos/vod/ipcam2/", "/home/centos/vod/ipcam3/")
heat_ts_folder = ("/home/centos/vod/heat1/", "/home/centos/vod/geat2/", "/home/centos/vod/heat3/")
ricoh_ts_folder = ("/home/centos/vod/ricoh1/", "/home/centos/vod/ricoh2/", "/home/centos/vod/ricoh3/")
destDir = 's3hecas/vod/ricoh1/'
bucketname = 's3hecas'
count = 0

# def ipcamEncoding():
for root, subdir, files in os.walk(ricoh_ts_folder[0]):
    for file in files:
        # print (file)
        if (file.split(".")[-1].lower() == 'ts'):
            filePath = os.path.join(root, file)
            mp4FilePath = os.path.join(root, os.path.splitext(file)[0] + ".mp4")
            # mp4file = os.path.join(mp4FilePath)
            print (mp4FilePath)
            # os.remove(mp4file)
            # s3 = boto3.resource('s3')
            # s3.meta.client.upload_file(mp4FilePath, bucketname, destDir+mp4file)
            # if os.path.isfile(mp4FilePath):
            #     continue
            # os.system("ffmpeg -i " + "\"" + filePath + "\"" + " \"" + mp4FilePath + "\"")
            # file = os.path.join(root, file)
            # os.remove(file)
            # count = count + 1
print ("Done the total number of file was be converted: ", count)
