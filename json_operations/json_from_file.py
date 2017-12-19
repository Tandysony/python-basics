# JSON file operations
## The JSON data is generated at https://www.mockaroo.com/

import json
from os import getcwd 

print(getcwd()) # print current directory

with open('json_operations/users.json', 'r') as f:
    data = json.load(f)

for user in data['users']:
    print(user['ip_address'], user['is_staff'])
    del user['is_staff']

with open('json_operations/new_users.json', 'w') as f:
    json.dump(data, f, indent=2)  # dump with indent

## SUMMARY
# 1. When load and dump json files, use "json.load(), json.dump()"
# 2. If "open('file_path')" raises "IOError: [Errno 2] No such file or directory: 'aa.bb' ", use "getcwd()" to double check the current working direcory.