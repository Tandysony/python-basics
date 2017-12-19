### Based on Corey Schafer's tutorial: https://www.youtube.com/watch?v=K8L6KVGG-7o&t=1561s
import re

# -------- BEGIN: simple data -------- #

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

stringx = 'Start a sentence and then bring it to an end'

# -------- END: simple data -------- #

pattern = re.compile(r'\[')

matches = pattern.finditer(text_to_search)

for match in matches:
    print("matched at {}; match is: {}".format(match.regs[0], text_to_search[match.regs[0][0]:match.regs[0][1]]))



## SUMMARY
# 1. When buiding the pattern, pay attention to what you are search: raw data (r'xxx') match or not.
# 2. The "__str__" is a special built-in method can be overridden. 
# 3. When calling a method, do not forget "()" at the end