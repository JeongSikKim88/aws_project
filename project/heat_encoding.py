# This Python file uses the following encoding: utf-8
import os, sys
from multiprocessing import Process
import boto3
from botocore.client import Config


# def ipcamEncoding(ipcam_ts_folder):
#     ACCESS_KEY_ID = 'AKIAJOPAUEHIGF4YP2HQ'
#     ACCESS_SECRET_KEY = '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'
#     BUCKET_NAME = 's3hecas'
#     FILE_FOLDER = ("/home/centos/vod/ipcam1/", "/home/centos/vod/ipcam2/", "/home/centos/vod/ipcam3/")
#     count = 0
#
#     for root, subdir, files in os.walk(ipcam_ts_folder):
#         for file in files:
#             if (file.split(".")[-1].lower() == 'ts'):
#                 filePath = os.path.join(root, file)
#                 mp4FilePath = os.path.join(root, os.path.splitext(file)[0] + ".mp4")
#                 if os.path.isfile(mp4FilePath):
#                     continue
#                 os.system("./ffmpeg1 -i " + "\"" + filePath + "\"" + " \"" + mp4FilePath + "\"")
#                 file = os.path.join(root, file)
#                 os.remove(file)
#                 count = count + 1
#
#                 for root, subdir, files in os.walk(FILE_FOLDER[0]):
#                     for file in files:
#                         if (file.split(".")[-1].lower() == 'mp4'):
#                             files = os.path.join(root, file)
#
#                             print(files)
#                             data = open(files, 'rb')
#
#                             # S3 Connect
#                             s3 = boto3.resource(
#                                 's3',
#                                 aws_access_key_id=ACCESS_KEY_ID,
#                                 aws_secret_access_key=ACCESS_SECRET_KEY,
#                                 config=Config(signature_version='s3v4')
#                             )
#
#                             # Image Uploaded
#                             s3.Bucket(BUCKET_NAME).put_object(Key='vod/ipcam1/' + file, Body=data, ACL='public-read')
#                             files = os.path.join(root, file)
#                             os.remove(files)
#                             print ("Done")
#
#                 for root, subdir, files in os.walk(FILE_FOLDER[1]):
#                     for file in files:
#                         if (file.split(".")[-1].lower() == 'mp4'):
#                             file = os.path.join(root, file)
#
#                             print(files)
#                             data = open(files, 'rb')
#
#                             # S3 Connect
#                             s3 = boto3.resource(
#                                 's3',
#                                 aws_access_key_id=ACCESS_KEY_ID,
#                                 aws_secret_access_key=ACCESS_SECRET_KEY,
#                                 config=Config(signature_version='s3v4')
#                             )
#
#                             # Image Uploaded
#                             s3.Bucket(BUCKET_NAME).put_object(Key='vod/ipcam2/' + files, Body=data, ACL='public-read')
#                             files = os.path.join(root, file)
#                             os.remove(files)
#                             print ("Done")
#
#                 for root, subdir, files in os.walk(FILE_FOLDER[2]):
#                     for file in files:
#                         if (file.split(".")[-1].lower() == 'mp4'):
#                             files = os.path.join(root, file)
#
#                             print(files)
#                             data = open(files, 'rb')
#
#                             # S3 Connect
#                             s3 = boto3.resource(
#                                 's3',
#                                 aws_access_key_id=ACCESS_KEY_ID,
#                                 aws_secret_access_key=ACCESS_SECRET_KEY,
#                                 config=Config(signature_version='s3v4')
#                             )
#
#                             # Image Uploaded
#                             s3.Bucket(BUCKET_NAME).put_object(Key='vod/ipcam3/' + files, Body=data, ACL='public-read')
#                             files = os.path.join(root, file)
#                             os.remove(files)
#                             print ("Done")
#
#     print ("Done the total number of file was be converted: ", count)


def heatEncoding(heat_ts_folder):
    ACCESS_KEY_ID = 'AKIAJOPAUEHIGF4YP2HQ'
    ACCESS_SECRET_KEY = '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'
    BUCKET_NAME = 's3hecas'
    FILE_FOLDER = ("/home/centos/vod/heat1/", "/home/centos/vod/heat2/", "/home/centos/vod/heat3/")
    count = 0
    for root, subdir, files in os.walk(heat_ts_folder):
        for file in files:
            if (file.split(".")[-1].lower() == 'ts'):
                filePath = os.path.join(root, file)
                mp4FilePath = os.path.join(root, os.path.splitext(file)[0] + ".mp4")
                if os.path.isfile(mp4FilePath):
                    continue
                os.system("./ffmpeg2 -i " + "\"" + filePath + "\" " + "-vcodec copy " + " \"" + mp4FilePath + "\"")
                filePath = os.path.join(root, file)
                print (filePath)
                try:
                    os.remove(filePath)
                except:
                    continue
                count = count + 1

            for root, subdir, files in os.walk(FILE_FOLDER[0]):
                for file in files:
                    if (file.split(".")[-1].lower() == 'mp4'):
                        files = os.path.join(root, file)

                        print(files)
                        data = open(files, 'rb')

                        # S3 Connect
                        s3 = boto3.resource(
                            's3',
                            aws_access_key_id=ACCESS_KEY_ID,
                            aws_secret_access_key=ACCESS_SECRET_KEY,
                            config=Config(signature_version='s3v4')
                        )

                        # Image Uploaded
                        s3.Bucket(BUCKET_NAME).put_object(Key='vod/heat1/' + files, Body=data, ACL='public-read',
                                                          ContentType='video/mp4')
                        files = os.path.join(root, file)
                        os.remove(files)
                        print ("Done")

            for root, subdir, files in os.walk(FILE_FOLDER[1]):
                for file in files:
                    if (file.split(".")[-1].lower() == 'mp4'):
                        files = os.path.join(root, file)

                        print(files)
                        data = open(files, 'rb')

                        # S3 Connect
                        s3 = boto3.resource(
                            's3',
                            aws_access_key_id=ACCESS_KEY_ID,
                            aws_secret_access_key=ACCESS_SECRET_KEY,
                            config=Config(signature_version='s3v4')
                        )

                        # Image Uploaded
                        s3.Bucket(BUCKET_NAME).put_object(Key='vod/heat2/' + files, Body=data, ACL='public-read',
                                                          ContentType='video/mp4')
                        files = os.path.join(root, file)
                        os.remove(files)
                        print ("Done")

            for root, subdir, files in os.walk(FILE_FOLDER[2]):
                for file in files:
                    if (file.split(".")[-1].lower() == 'mp4'):
                        files = os.path.join(root, file)

                        print(files)
                        data = open(files, 'rb')

                        # S3 Connect
                        s3 = boto3.resource(
                            's3',
                            aws_access_key_id=ACCESS_KEY_ID,
                            aws_secret_access_key=ACCESS_SECRET_KEY,
                            config=Config(signature_version='s3v4')
                        )

                        # Image Uploaded
                        s3.Bucket(BUCKET_NAME).put_object(Key='vod/heat3/' + files, Body=data, ACL='public-read',
                                                          ContentType='video/mp4')
                        files = os.path.join(root, file)
                        os.remove(files)
                        print ("Done")

    print ("Done the total number of file was be converted: ", count)


# def ricohEncoding(ricoh_ts_folder):
#     count = 0
#     for root, subdir, files in os.walk(ricoh_ts_folder):
#         for file in files:
#             if (file.split(".")[-1].lower() == 'ts'):
#                 filePath = os.path.join(root, file)
#                 mp4FilePath = os.path.join(root, os.path.splitext(file)[0] + ".mp4")
#                 if os.path.isfile(mp4FilePath):
#                     continue
#                 os.system("./ffmpeg3 -i " + "\"" + filePath + "\"" + " \"" + mp4FilePath + "\"")
#                 file = os.path.join(root, file)
#                 os.remove(file)
#                 count = count + 1
#     print ("Done the total number of file was be converted: ", count)


if __name__ == '__main__':
    # ipcam_ts_folder = ("/home/centos/vod/ipcam1/", "/home/centos/vod/ipcam2/", "/home/centos/vod/ipcam3/")
    heat_ts_folder = ("/home/centos/vod/heat1/", "/home/centos/vod/heat2/", "/home/centos/vod/heat3/")
    # ricoh_ts_folder = ("/home/centos/vod/ricoh1/", "/home/centos/vod/ricoh2/", "/home/centos/vod/ricoh3/")
    # pr1 = Process(target=ipcamEncoding(ipcam_ts_folder[0]))
    # pr2 = Process(target=heatEncoding(ipcam_ts_folder[1]))
    # pr3 = Process(target=ricohEncoding(ricoh_ts_folder[0]))
    # pr4 = Process(target=ricohEncoding(ricoh_ts_folder[1]))
    pr5 = Process(target=heatEncoding(heat_ts_folder[0]))
    pr6 = Process(target=heatEncoding(heat_ts_folder[1]))
    pr7 = Process(target=heatEncoding(heat_ts_folder[2]))
    # pr1.start()
    # pr2.start()
    # pr3.start()
    # pr4.start()
    while true:
        pr5.start()
        pr6.start()
        pr7.start()
    # pr1.join()
    # pr2.join()
    # pr3.join()
    # pr4.join()
    # pr5.join()
    # pr6.join()
