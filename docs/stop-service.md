# Stop Service #

## Request ##
POST /
Body:
```
[
  {
    "id": "i-019ebfaf92631c228",
    "serviceName": "nodejs-restart"
  }    
]
```

## Response ##

Body:
```
{
  "executionTime": 389,
  "request": [
    {
        "serviceName": "nodejs-restart",
        "id": "i-019ebfaf92631c228"
    }
  ]
}
```