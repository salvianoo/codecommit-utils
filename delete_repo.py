import sys
import boto3

client = boto3.client('codecommit')

def delete_repository(name, description=''):
    return client.delete_repository(
        repositoryName=name,
    )

name = sys.argv[1]

response = delete_repository(name)
print response
