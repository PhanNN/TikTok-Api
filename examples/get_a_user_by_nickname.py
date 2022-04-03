from TikTokApi import TikTokApi
import sys
import json

username = sys.argv[1]
# cookies = json.loads(sys.argv[2])

api = TikTokApi.get_instance()

print(json.dumps(api.get_user(
  username = username
  # , custom_cookies = cookies
)))
