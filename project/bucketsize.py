import boto3

def get_folder_size(bucket, prefix):
    total_size = 0
    for obj in boto3.resource('s3hecas').Bucket(bucket).objects.filter(Prefix=prefix):
        total_size += obj.size
    return total_size