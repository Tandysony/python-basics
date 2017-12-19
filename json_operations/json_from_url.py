# JSON data from a URL

import json
from urllib2 import urlopen

response = urlopen("https://api.github.com/search/repositories?q=iphonex")
source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))
print (len(data['items']))

for item in data['items']:
    print("Repo Name: {}.\t\t\t Clone it at: {}".format(item['clone_url'], item['git_refs_url']))