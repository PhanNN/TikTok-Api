from TikTokApi import TikTokApi
import sys
import json

api = TikTokApi.get_instance()

# headers
# {
#     "cookie": ""
# }

# params
# {
#     "keyword": "",
#     "offset": 12
# }

headers = json.loads(sys.argv[1])
params = json.loads(sys.argv[2])

print(json.dumps(
    api.get_tiktoks_by_keyword(headers, params)
))
