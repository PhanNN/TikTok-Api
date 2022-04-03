from TikTokApi import TikTokApi
import sys
import json

headers = json.loads(sys.argv[1])
params = json.loads(sys.argv[2])

api = TikTokApi.get_instance()
print(json.dumps(api.get_comments(
  headers = headers,
  params = params
)))