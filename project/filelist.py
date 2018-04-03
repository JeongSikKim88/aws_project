import boto3
from botocore.client import Config
import pymysql

ACCESS_KEY_ID = 'AKIAJOPAUEHIGF4YP2HQ'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 's3hecas'

print ('--- Connecting to S3')
# S3 Connect
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

print ('--- Selecting the bucket')
bucket = s3.Bucket(BUCKET_NAME)


print ('--- List all bucket key versions')
for object in bucket.objects.all():
    print (object.key)

conn = pymysql.connect(host='localhost', user='root', password='hecas1234!',
                       db='vod', charset='utf8')

# curs = conn.cursor()
# sql = """insert into customer(name,category,region)
#          values (%s, %s, %s)"""
# curs.execute(sql, ('홍길동', 1, '서울'))
# curs.execute(sql, ('이연수', 2, '서울'))
# conn.commit()
#
# conn.close()