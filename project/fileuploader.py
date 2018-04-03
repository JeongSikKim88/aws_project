# This Python file uses the following encoding: utf-8
import boto3
import boto.s3
import sys, os, base64, datetime, hashlib, hmac, urllib
import botocore
from botocore.client import Config

# # Fill these in - you get them when you sign up for S3
# AWS_ACCESS_KEY_ID = 'AKIAJOPAUEHIGF4YP2HQ'
# AWS_ACCESS_KEY_SECRET = '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'
# Fill in info on data to upload
# destination bucket name
bucket_name = 's3hecas'
# source directory
sourceDir = '/home/centos/vod/ricoh2/'
# destination directory name (on s3)
destDir = 'vod/ricoh2/'

# max size in bytes before uploading in parts. between 1 and 5 GB recommended
MAX_SIZE = 20 * 1000 * 1000
# size of parts when uploading in parts
PART_SIZE = 6 * 1000 * 1000

# # Other valid options here are 'auto' (default) and 'virtual'
# s3 = boto3.client('s3', 'us-west-2', config=Config(s3={'addressing_style': 'path'}))

# conn = boto.connect_s3(aws_access_key_id, aws_secret_access_key)

# s3 = boto3.client('s3', config=Config(signature_version='s3v4'))
s3 = boto3.resource('s3')
# file = os.walk(sourceDir)
# s3.meta.client.upload_file(file, bucket_name, 's3hecas/vod/ipcam1/Fri\ Dec\ 22\ 16\:08\:05\ 2017.mp4')

# bucket = s3.create_bucket(bucket_name,
#                             location=boto.s3.connection.Location.DEFAULT)

uploadFileNames = []
for (sourceDir, dirname, filename) in os.walk(sourceDir):
    uploadFileNames.extend(filename)
    break


def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


for filename in uploadFileNames:
    sourcepath = os.path.join(sourceDir + filename)
    destpath = os.path.join(destDir, filename)
    print ('Uploading %s to Amazon S3 bucket %s' % \
           (sourcepath, bucket_name))

    filesize = os.path.getsize(sourcepath)
    if filesize > MAX_SIZE:
        print ("multipart upload")
        # mp = s3.MultipartUpload(bucket_name, destpath, '549a0c55b612865fa57b0eeedd4c187b11695353f7036804b85ca77ef3e6a245')
        fp = open(sourcepath, 'rb')
        fp_num = 0
        while (fp.tell() < filesize):
            fp_num += 1
            print ("uploading part %i" % fp_num)
            # mp.upload_part_from_file(fp, fp_num, cb=percent_cb, num_cb=10, size=PART_SIZE)
            # mp.multipart_upload_part = s3.MultipartUploadPart(bucket_name,destpath,'549a0c55b612865fa57b0eeedd4c187b11695353f7036804b85ca77ef3e6a245','part_number')
            multipart_upload = s3.MultipartUpload(bucket_name, destpath, '549a0c55b612865fa57b0eeedd4c187b11695353f7036804b85ca77ef3e6a245')
        multipart_upload.complete_upload()

    else:
        print ("singlepart upload")
        k = boto.s3.key.Key(bucket_name)
        k.key = destpath
        k.set_contents_from_filename(sourcepath,
                                     cb=percent_cb, num_cb=10)
