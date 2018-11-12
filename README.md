# TweetScraper [![Build Status](https://travis-ci.org/bestreyer/TweetScraper.svg?branch=master)](https://travis-ci.org/bestreyer/TweetScraper)

TweetScraper is a serverless application for scraping tweets from twitter by hashtag or username

![Serverless chart](docs/serverless.png)

## Why serverless ?

- No need to manage a server
- No need to fire alerts or write scripts to scale up and down
- Don't have to pay for idle capacity


## Sandbox

Get tweets by hashtag - https://gyexpx2j0m.execute-api.eu-central-1.amazonaws.com/Prod/hashtags/<hashtag>

Get tweets by username - https://gyexpx2j0m.execute-api.eu-central-1.amazonaws.com/Prod/users/<username>

## CI
https://travis-ci.org/bestreyer/TweetScraper

## Run locally

### Requirements
- python 3.6 with venv
- [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- make
- docker

### Create environment
```bash
python3 -m venv venv
source ./venv/bin/activate
```

### Run api
```bash
make start_api
```

### Run tests
```bash
make unit_tests
```

## Packaging and deployment
```bash
make build
sam package --template-file template.yaml --s3-bucket <s3-bucket-name> --output-template-file packaged.yaml
sam deploy --template-file ./packaged.yaml --stack-name <stackname> --capabilities CAPABILITY_IAM
``` 

