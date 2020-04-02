[![CircleCI](https://circleci.com/gh/GovWizely/lambda-errors/tree/master.svg?style=svg)](https://circleci.com/gh/GovWizely/lambda-errors/tree/master)

[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=GovWizely/lambda-errors)](https://dependabot.com)

# Lambda Errors

This project provides an AWS Lambda based on [this blueprint](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/function/configure/blueprint?blueprint=cloudwatch-alarm-to-slack-python) that captures a Cloudwatch alarm via SNS and publishes an alert to a Slack channel.

## Prerequisites

- This project is tested against Python 3.7+ in [CircleCI](https://app.circleci.com/github/GovWizely/lambda-errors/pipelines).

## Getting Started

	git clone git@github.com:GovWizely/lambda-errors.git
	cd lambda-errors
	mkvirtualenv -p /usr/local/bin/python3.8 -r requirements-test.txt errors

If you are using PyCharm, make sure you enable code compatibility inspections for Python 3.7/3.8.

### Tests

```bash
python -m pytest
```

## Configuration

* Define the Slack hook URL and channel as environment variables e.g. `export hookUrl=hooks.slack.com/services/abc`. This will allow you to run the Lambda locally.
* Define AWS credentials in either `config.yaml` or in the [default] section of `~/.aws/credentials`. To use another profile, you can do something like `export AWS_DEFAULT_PROFILE=govwizely`.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the AWS credentials to version control.

## Invocation

	lambda invoke -v
 
## Deploy
    
To deploy:

	lambda deploy --requirements requirements.txt
