import requests
# import json
#
# class postcodes:
#     def __init__(self):
#         self.base_url =
#         self.postcode = ''
#         self.
#

post_codes_req = requests.get("https://api.postcodes.io/postcodes/rh162qd")

print(post_codes_req.status_code)
print(post_codes_req.headers)
print(type(post_codes_req.content))
print(post_codes_req.content)
print(type(post_codes_req.json()))
print(post_codes_req.json())

#DO FOR HOMEWORK TONIGHT