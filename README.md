# Aws Chaos Beaver #

# Overview #
* Simulate service/process failures to validate stack reliability
* Remove port from firewalld to simulate network failure
* The function is to stop a service, to kill a process, or block incoming traffic to verify how overall application stack survives partial failures

# Components #
* Aws Lambda
* Boto3 Python Api for [SSM](http://boto3.readthedocs.io/en/latest/reference/services/ssm.html)
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

## Describe Instance ##
* To verify the ssm agent is installed and proper roles are provisioned for Lambda function and for ec2 instance
```
aws lambda invoke \
--invocation-type RequestResponse \
--function-name smith-poc-chaos-beaver \
--region us-east-2 \
--payload '{
    "method": "get",
    "path": "/instance/i-0b314f9c31a99621c,i-09b496a3f86dfac11"
  }' \
  $(tty)
```

## Stop Service - Linux ##
```
aws lambda invoke \
--invocation-type RequestResponse \
--function-name smith-poc-chaos-beaver \
--region us-east-2 \
--payload '{
    "method": "delete",
    "path": "/service",
    "body": {
      "instanceId": "i-0b314f9c31a99621c",
      "osType": "Linux",
      "serviceName": "nodejs-restart"
    }
  }' \
  $(tty)
```
## Stop Service - Windows ##
```
aws lambda invoke \
--invocation-type RequestResponse \
--function-name smith-poc-chaos-beaver \
--region us-east-2 \
--payload '{
    "method": "delete",
    "path": "/service",
    "body": {
      "instanceId": "i-09b496a3f86dfac11",
      "osType": "Win",
      "serviceName": "mssqlserver"
    }
  }' \
  $(tty)
```

## Kill Process By Name ##
```
aws lambda invoke \
--invocation-type RequestResponse \
--function-name smith-poc-chaos-beaver \
--region us-east-2 \
--payload '{
    "method": "delete",
    "path": "/process",
    "body": {
      "instanceId": "i-0b314f9c31a99621c",
      "osType": "Linux",
      "processName": "node"
    }
  }' \
  $(tty)
```

## Kill Process By Port ##
* Note forever-service or other watch process may restart the process right away
```
aws lambda invoke \
--invocation-type RequestResponse \
--function-name smith-poc-chaos-beaver \
--region us-east-2 \
--payload '{
    "method": "delete",
    "path": "/process",
    "body": {
      "instanceId": "i-0b314f9c31a99621c",
      "osType": "Linux",
      "portNumber": 3000
    }
  }' \
  $(tty)
```


## Kill Process By Name and Port ##
* Note forever-service or other watch process may restart the process right away
```
aws lambda invoke \
--invocation-type RequestResponse \
--function-name smith-poc-chaos-beaver \
--region us-east-2 \
--payload '{
    "method": "delete",
    "path": "/process",
    "body": {
      "instanceId": "i-0b314f9c31a99621c",
      "osType": "Linux",
      "processName": "node",
      "portNumber": 3000
    }
  }' \
  $(tty)
```

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

* Install awscli: ```sudo pip install awscli```
* Deploy to existing aws lambda function: ```./aws/deploy-lambda```
* For IAM policies required for ec2 instances and for lamba function see Configuration section of the readme

