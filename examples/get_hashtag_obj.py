from TikTokApi import TikTokApi
import sys
import json

api = TikTokApi.get_instance()

hashtag = sys.argv[1]

print(
    json.dumps(api.get_hashtag_object(hashtag = hashtag))
)
