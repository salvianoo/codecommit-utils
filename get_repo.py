import sys
import json
from bson import json_util

import boto3

client = boto3.client('codecommit')

def get_repository(name):
    return client.get_repository(
        repositoryName=name
    )

name = sys.argv[1]

response = get_repository(name)
print json.dumps(response, default=json_util.default)
# print response
