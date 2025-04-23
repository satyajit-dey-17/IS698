import boto3

def list_s3_files(bucket_name):
    """List all files in an S3 bucket."""
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print("\nFiles in S3 Bucket:")
            for file in response['Contents']:
                print(f"- {file['Key']} (Size: {file['Size']} bytes)")
        else:
            print("No files found in the bucket.")
    except Exception as e:
        print(f"Error listing S3 files: {e}")

def create_dynamodb_table(table_name):
    """Create a DynamoDB table."""
    dynamodb = boto3.client('dynamodb')
    try:
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}  # Partition key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'N'}  # Numeric ID
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print(f"\nDynamoDB Table '{table_name}' created successfully!")
        return response
    except Exception as e:
        print(f"Error creating DynamoDB table: {e}")

def insert_dynamodb_item(table_name, item_data):
    """Insert an item into a DynamoDB table."""
    dynamodb = boto3.resource('dynamodb')
    try:
        table = dynamodb.Table(table_name)
        response = table.put_item(Item=item_data)
        print(f"\nItem inserted into DynamoDB table '{table_name}':")
        print(item_data)
        return response
    except Exception as e:
        print(f"Error inserting item into DynamoDB: {e}")

if __name__ == "__main__":
    # Example usage
    s3_bucket = "your-bucket-name"  # Replace with your bucket
    dynamodb_table = "TestTable"    # Replace if needed
    item_to_insert = {
        "id": 1,
        "name": "Sample Item",
        "description": "This is a test item."
    }

    list_s3_files(s3_bucket)
    create_dynamodb_table(dynamodb_table)
    insert_dynamodb_item(dynamodb_table, item_to_insert)
