# Kill Process By Name and By Port Number #

## Request ##
POST /
Body:
```
[
	{
    "id": "i-0b314f9c31a99621c",
    "processName": "node",
    "portNumber": 3000
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
        "processName": "node",
        "id": "i-0b314f9c31a99621c"
    }
  ]
}
```