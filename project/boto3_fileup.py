import os
import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAJOPAUEHIGF4YP2HQ'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 's3hecas'
FILE_FOLDER = '/home/centos/vod/ipcam3/';
# file_name = os.walk(FILE_FOLDER)

for root, subdir, files in os.walk(FILE_FOLDER):
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
            s3.Bucket(BUCKET_NAME).put_object(Key='vod/ipcam3/' + files, Body=data, ACL='public-read')
            files = os.path.join(root, file)
            os.remove(files)

            print ("Done")
