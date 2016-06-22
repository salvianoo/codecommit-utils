import sys
import boto3

client = boto3.client('codecommit')

def create_repository(name, description=''):
    return client.create_repository (
        repositoryName=name,
        repositoryDescription=description
    )

name = sys.argv[1]

try:
    sys.argv[2]
except IndexError:
    description = ''
else:
    description = sys.argv[2]

response = create_repository(name, description)
print response
