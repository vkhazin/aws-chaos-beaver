# Kill Process By Port Number #

## Request ##
POST /
Body:
```
[
	{
    "id": "i-0b314f9c31a99621c",
    "portNumber": "3000"
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
        "portNumber": "3000",
        "id": "i-0b314f9c31a99621c"
    }
  ]
}
```