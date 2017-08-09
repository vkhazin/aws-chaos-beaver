# Aws Chaos Beaver #

# Overview #
* Simulate service/process failures to validate stack reliability
* The end-point is to stop a service or to kill a process to verify how overall application stack survives partial failures

# Components #
* Api Gateway + Aws Lambda
* Boto3 Python Api for [SSM](http://boto3.readthedocs.io/en/latest/reference/services/ssm.html)
* The Easiest way to build end-points yet using [AWS Chalice](http://chalice.readthedocs.io/en/latest/) and python
* CloudWatch logs and Api Gateway Logging for troubleshooting

# Configuration #
* [Install ssm agent on ec2 instances](https://gist.github.com/vkhazin/100c717b9780fc8f7eaf444d4d6b339f)
* Add AmazonEC2RoleforSSM policy to ec2 instances role
* Add AmazonSSMFullAccess policy to lambda execution role
* Lambda function shall be deployed in the same region where the ec2 instances are, otherwise following error may pop-up:
```
{
  "Message": "ChaliceViewError: An error occurred (InvalidInstanceId) when calling the SendCommand operation: ",
  "Code": "ChaliceViewError"
}
```

# End-Points #

## [Echo](./docs/echo.md) ##

## [Stop Service](./docs/stop-service.md) ##

## [Kill Process By Name](./docs/kill-process-by-name.md) ##

## [Kill Process By Port Number](./docs/kill-service-by-port.md) ##

## [Kill Process By Name and Port](./docs/kill-process-by-name-port.md) ##

# Unit Testing #

* ./test folder contains unit test using python unittest
* running locally: ```chalice local```

# Deployment #

* Double check settings in ./.chalice/config.json file
* From terminal run: ```chalice deploy``` and output will list api-gateway end-point