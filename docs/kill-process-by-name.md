# Kill Process By Name #

## Request ##
POST /
Body:
```
[
	{
    "id": "i-0b314f9c31a99621c",
    "processName": "node"
  }    
]
```

## Response ##

Body:
```
{
  "executionTime": 432,
  "request": [
    {
        "processName": "node",
        "id": "i-0b314f9c31a99621c"
    }
  ]
}
```