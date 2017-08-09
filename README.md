# Aws Chaos Beaver #

# Overview #
* Simulate service/process failures to validate stack reliability
* The end-point is to stop a service or to kill a process to verify how overall application stack survives partial failures

# Components #
* Api Gateway + Aws Lambda
* Boto3 Python Api for [SSM](http://boto3.readthedocs.io/en/latest/reference/services/ssm.html)
* The Easiest way to build end-points yet using [AWS Chalice](http://chalice.readthedocs.io/en/latest/) and python
* CloudWatch logs and Api Gateway Logging for troubleshooting

# End-Points #

## [Echo](./doc/echo.md) ##

## [Stop Service](./doc/stop-service.md) ##

## [Kill Process By Name](./doc/kill-process-by-name.md) ##

## [Kill Process By Port Number](./doc/kill-process-by-port.md) ##

## [Kill Process By Name and Port](./doc/kill-process-by-name-port.md) ##

# Unit Testing #

* ./test folder contains unit test using python unittest
* running locally: ```chalice local```

# Deployment #

* Double check settings in ./.chalice/config.json file
* From terminal run: ```chalice deploy``` and output will list api-gateway end-point