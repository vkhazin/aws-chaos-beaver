# Aws Chaos Beaver #

# Overview #
* Simulate service/process failures to validate stack reliability 
* Execute arbitrary shell commands on ec2 instances using [SSM agent](http://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html)

# Components #
* Api Gateway + Aws Lambda
* Boto3 Python Api for [SSM](http://boto3.readthedocs.io/en/latest/reference/services/ssm.html)
* CloudWatch logs to trace actions
