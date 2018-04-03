# This Python file uses the following encoding: utf-8
import os, sys
from multiprocessing import Process


def ipcamEncoding(ipcam_ts_folder):
    count = 0
    for root, subdir, files in os.walk(ipcam_ts_folder):
        for file in files:
            if (file.split(".")[-1].lower() == 'ts'):
                filePath = os.path.join(root, file)
                mp4FilePath = os.path.join(root, os.path.splitext(file)[0] + ".mp4")
                if os.path.isfile(mp4FilePath):
                    continue
                os.system("./ffmpeg1 -i " + "\"" + filePath + "\"" + " \"" + mp4FilePath + "\"")
                file = os.path.join(root, file)
                os.remove(file)
                count = count + 1

    print ("Done the total number of file was be converted: ", count)


def heatEncoding(heat_ts_folder):
    count = 0
    for root, subdir, files in os.walk(heat_ts_folder):
        for file in files:
            if (file.split(".")[-1].lower() == 'ts'):
                filePath = os.path.join(root, file)
                mp4FilePath = os.path.join(root, os.path.splitext(file)[0] + ".mp4")
                if os.path.isfile(mp4FilePath):
                    continue
                os.system("./ffmpeg2 -i " + "\"" + filePath + "\"" + " \"" + mp4FilePath + "\"")
                file = os.path.join(root, file)
                os.remove(file)
                count = count + 1
    print ("Done the total number of file was be converted: ", count)


def ricohEncoding(ricoh_ts_folder):
    count = 0
    for root, subdir, files in os.walk(ricoh_ts_folder):
        for file in files:
            if (file.split(".")[-1].lower() == 'ts'):
                filePath = os.path.join(root, file)
                mp4FilePath = os.path.join(root, os.path.splitext(file)[0] + ".mp4")
                if os.path.isfile(mp4FilePath):
                    continue
                os.system("./ffmpeg3 -i " + "\"" + filePath + "\"" + " \"" + mp4FilePath + "\"")
                file = os.path.join(root, file)
                os.remove(file)
                count = count + 1
    print ("Done the total number of file was be converted: ", count)


if __name__ == '__main__':
    ipcam_ts_folder = ("/home/centos/vod/ipcam1/", "/home/centos/vod/ipcam2/", "/home/centos/vod/ipcam3/")
    heat_ts_folder = ("/home/centos/vod/heat1/", "/home/centos/vod/heat2/", "/home/centos/vod/heat3/")
    ricoh_ts_folder = ("/home/centos/vod/ricoh1/", "/home/centos/vod/ricoh2/", "/home/centos/vod/ricoh3/")
    pr1 = Process(target=ipcamEncoding(ipcam_ts_folder[0]))
    pr2 = Process(target=heatEncoding(ipcam_ts_folder[1]))
    pr3 = Process(target=ricohEncoding(ricoh_ts_folder[0]))
    pr4 = Process(target=ricohEncoding(ricoh_ts_folder[1]))
    pr5 = Process(target=ricohEncoding(heat_ts_folder[0]))
    pr6 = Process(target=ricohEncoding(heat_ts_folder[1]))
    pr1.start()
    pr2.start()
    pr3.start()
    pr4.start()
    pr5.start()
    pr6.start()
    pr1.join()
    pr2.join()
    pr3.join()
    pr4.join()
    pr5.join()
    pr6.join()