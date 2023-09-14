from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class CustomS3Boto3Storage(S3Boto3Storage):
    location = settings.AWS_MEDIA_LOCATION


