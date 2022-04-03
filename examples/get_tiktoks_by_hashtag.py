from TikTokApi import TikTokApi
import json
import sys

api = TikTokApi.get_instance()

id=sys.argv[1]
pageSize=sys.argv[2]
fromCursor=sys.argv[3]

print(
    json.dumps(
        api.hashtag_page(
            hashtag_id=id,
            count=pageSize,
            offset=fromCursor,
        )
    )
)

# api = TikTokApi.get_instance()

# count = 30

# tiktoks = api.by_hashtag("funny", count=count)

# for tiktok in tiktoks:
#     print(tiktok)
