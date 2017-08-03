# Aws Chaos Beaver #

# Overview #
* Simulate service/process failures to validate stack reliability
* The end-point is to stop a service or to kill a process to verify how overall application stack survives partial failures

# Components #
* Api Gateway + Aws Lambda
* Boto3 Python Api for [SSM](http://boto3.readthedocs.io/en/latest/reference/services/ssm.html)
* The Easiest way to build end-points yet using [AWS Chalice](http://chalice.readthedocs.io/en/latest/) and python
* CloudWatch logs and Api Gateway Logging for troubleshooting

# End-Point #

## Request ##
Header: {'x-api-key': '7cc6f8fa-248c-4685-a2ba-7fe47e18fc9c'}  
POST /  
```
Body: [
  {
    "id": "i-0b314f9c31a99621c",
    "serviceName": "redis"
  },
  {
    "id": "i-0b314f9c31a99621c",
    "processName": "nodejs"
  },
  {
    "id": "i-0b314f9c31a99621c",
    "port": "3000"
  },  
]
```

## Response - Success ##
```
Body: {
  "Request": [
    {
      "id": "i-0b314f9c31a99621c",
      "serviceName": "redis"
    },
    {
      "id": "i-0b314f9c31a99621c",
      "processName": "nodejs"
    },
    {
      "id": "i-0b314f9c31a99621c",
      "port": "3000"
    },  
  ],
  'executionTime': 300
}
```
# Testing #

* ./test folder contains unit test using python unittest
* running locally: ```chalice local```

# Deployment #

* Double check settings in ./.chalice/config.json file
* From terminal run: ```chalice deploy``` and output will list api-gateway end-point