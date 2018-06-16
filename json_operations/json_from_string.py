# JSON object operations
## The JSON data is generated at https://www.mockaroo.com/

import json

user_string = '''
{ "user":
[{
  "id": 1,
  "first_name": "Kelly",
  "last_name": "Wolledge",
  "email": "kwolledge0@icio.us",
  "gender": "Male",
  "ip_address": "252.19.201.143",
  "is_stuff": false
}, {
  "id": 2,
  "first_name": "Staffard",
  "last_name": "Lesser",
  "email": "slesser1@cdbaby.com",
  "gender": "Female",
  "ip_address": null,
  "is_stuff": true
}, {
  "id": 3,
  "first_name": "Fulton",
  "last_name": "Gellan",
  "email": "fgellan2@oracle.com",
  "gender": "Male",
  "ip_address": "47.94.32.7",
  "is_stuff": true
}, {
  "id": 4,
  "first_name": "Brendon",
  "last_name": "Gorges",
  "email": "bgorges3@furl.net",
  "gender": "Male",
  "ip_address": "136.3.47.215",
  "is_stuff": true
}]
}
'''

data = json.loads(user_string)

print("{}\n".format(type(data["user"])))  # <type 'list'>

for user in data["user"]:
    print("{}".format(user["email"]))
    del user["email"]

new_string = json.dumps(data, indent=2, sort_keys=True)   # dump with format and sorting

print ("\n{}".format(new_string))





## SUMMARY
# 1. To work with a JSON string object, use "json.loads(), json.dumps()". Pay attention to the 's' before the left parentheses
# 2. The JSON decoder and endcoder are illustrated below:

## JSON Decoder
# -------------------------------
#  JSON	                Python
# -------------------------------
#  object               dict
#  array	            list
#  string               unicode
#  number (int)	        int, long
#  number (real)	    float
#  true                 True
#  false	            False
#  null	                None
# -------------------------------

## JSON Encoder
# -------------------------------
#  Python               JSON
# -------------------------------
#  dict                 object
#  list, tuple          array
#  str, unicode         string
#  int, long, float     number
#  True                 true
#  False	            false
#  None                 null
# -------------------------------