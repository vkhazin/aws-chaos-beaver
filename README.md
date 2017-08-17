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
An error occurred (InvalidInstanceId) when calling the SendCommand operation: "
```
* Firewalld and iptables need to be installed on the redhat instances:
```
sudo yum update -y && sudo yum install iptables firewalld -y
```
* To list active firewall rules: ```sudo firewall-cmd --list-all-zones```
* To open port permanently: ```sudo firewall-cmd --zone=public --add-port=3000/tcp --permanent```
* To close port temporarily: ```sudo firewall-cmd --zone=public --remove-port=3000/tcp```

# Invocation #

## Remove port from firewalld ##
```
aws lambda invoke \
--invocation-type RequestResponse \
--function-name smith-poc-chaos-beaver \
--region us-east-2 \
--payload '{
    "method": "delete",
    "path": "/port",
    "body": {
      "instanceId": "i-0b314f9c31a99621c",
      "osType": "Linux",
      "portNumber": 3000
    }
  }' \
  $(tty)
```

# Unit Testing #

* ./tests folder contains unit test using python unittest

# Deployment #

* Install awsclie: ```sudo pip install awscli```
* Deploy to existing aws lambda function: ```./aws/deploy-lambda```