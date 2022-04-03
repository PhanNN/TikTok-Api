from TikTokApi import TikTokApi
import json
import sys

videoId = sys.argv[1]

api = TikTokApi.get_instance()
result = api.get_tiktok_by_id(id=videoId)
print(
  json.dumps(api.get_tiktok_by_id(id=videoId))
)