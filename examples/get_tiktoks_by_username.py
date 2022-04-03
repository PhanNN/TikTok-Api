from TikTokApi import TikTokApi
import sys
import json

api = TikTokApi.get_instance()

id=sys.argv[1]
secUid=sys.argv[2]
pageSize=sys.argv[3]
fromCursor=sys.argv[4]
# print(
#     json.dumps(
#         api.by_username(username=username, count=count)
#     )
# )

print(
    json.dumps(
        api.user_page(
            userID=id,
            secUID=secUid,
            page_size=pageSize,
            cursor=fromCursor,
        )
    )
)


# api = TikTokApi.get_instance()

# count = 30

# tiktoks = api.by_username("americanredcross", count=count)

# for tiktok in tiktoks:
#     print(tiktok)
