## Get Video's Comments Doc

### Required inputs
```
  headers: {
    "cookie": "",
    "custom_verifyFp": "",
    "custom_device_id": "",
    "ms_token": "",
    "x_bogus": ""
  },
  params: {
    "id": "", // video id
    "cursor": 0,
    "count": 20
  }
```

### Command
```
  python examples/get_comments.py ' _headers_ ' ' _params_ '
```

### Example
```
  python examples/get_comments.py '{"cookie": "", "custom_verifyFp": "", "custom_device_id": "", "ms_token": "", "x_bogus": ""}' '{"id": "", "cursor": 0, "count": 20}'
```