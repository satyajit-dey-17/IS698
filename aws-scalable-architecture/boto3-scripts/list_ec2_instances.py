import boto3

def main():
    ec2 = boto3.client('ec2')
    resp = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    for reservation in resp['Reservations']:
        for inst in reservation['Instances']:
            print(
                inst['InstanceId'],
                inst['InstanceType'],
                inst['State']['Name'],
                inst.get('PublicIpAddress', 'no public IP')
            )

if __name__ == '__main__':
    main()

