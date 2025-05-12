import boto3
from botocore.exceptions import ClientError

def main():
    s3 = boto3.client('s3')
    bucket = 'aq60258-proj-bckt'   # ← change to a globally unique name
    region = 'us-east-1'              # ← match your Terraform region

    try:
        if region == 'us-east-1':
            # us-east-1 doesn’t accept LocationConstraint
            s3.create_bucket(Bucket=bucket)
        else:
            s3.create_bucket(
                Bucket=bucket,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Created bucket: {bucket}")
    except ClientError as e:
        print(f"Error creating bucket: {e}")
        return

    # Upload a test file
    try:
        with open('test.txt', 'rb') as f:
            s3.upload_fileobj(f, bucket, 'test.txt')
        print("Uploaded test.txt")
    except ClientError as e:
        print(f"Error uploading test file: {e}")

if __name__ == '__main__':
    main()

