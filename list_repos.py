import json
import boto3

client = boto3.client('codecommit')

def list_repos():
    return client.list_repositories(
            sortBy='lastModifiedDate',
            order='descending'
        )

response = list_repos()
print json.dumps(response)
