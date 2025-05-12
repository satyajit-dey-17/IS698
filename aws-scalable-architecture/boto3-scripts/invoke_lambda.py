import boto3
import json

def main():
    client = boto3.client('lambda')
    resp = client.invoke(
        FunctionName='lambda-stack-LogUploads',  # ← match your stack/function name
        InvocationType='RequestResponse',
        Payload=json.dumps({})
    )
    body = resp['Payload'].read().decode()
    print("Lambda response:", body)

if __name__ == '__main__':
    main()

