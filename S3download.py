import boto3
import botocore

BUCKET_NAME = 'storage1training' # replace with your bucket name
FILE_NAME= 'Lesson - 1.pdf' # replace with the your specific file that exists in your bucket

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(FILE_NAME,FILE_NAME)
    print("Downloaded File : ",FILE_NAME," successfully from Bucket : ",BUCKET_NAME)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The File ",FILE_NAME," does not exist in Bucket : ",BUCKET_NAME)
    else:
        raise
