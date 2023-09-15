import boto3

from decouple import config
import boto3
from botocore.exceptions import NoCredentialsError

# Replace these with your own values
AWS_S3_ACCESS_KEY_ID = config("AWS_S3_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
# Create an S3 client with the desired region
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_S3_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name="us-east-1"  # Change this to your desired region
)

# Specify the object key of the file you want to retrieve
object_key = "static/css/main.css"  # Replace with the correct object key

try:
    # Download the object
    response = s3.get_object(Bucket=AWS_STORAGE_BUCKET_NAME, Key=object_key)
    file_content = response["Body"].read().decode("utf-8")

    # Now, file_content contains the content of the retrieved file (main.css)
    print(file_content)

except NoCredentialsError:
    print("No AWS credentials found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")