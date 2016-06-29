#!/bin/bash

#AWS
# CodeCommit
alias create-repository='aws codecommit create-repository --repository-name'
alias list-repositories='aws codecommit list-repositories --sort-by lastModifiedDate --order descending'
alias get-repository='aws codecommit get-repository --repository-name'
alias delete-repository='aws codecommit delete-repository --repository-name'

#Print clone url
aws codecommit get-repository --repository-name <name> --query repositoryMetadata.cloneUrlSsh | tr -d "\""

#List repositories names
aws codecommit list-repositories --sort-by lastModifiedDate --order descending --query repositories[].repositoryName[]
