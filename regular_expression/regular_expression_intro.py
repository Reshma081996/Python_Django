#regular EXpression- pattern matching

#step 1 import re mdule
from re import *

pattern="ab"
matcher=finditer(pattern,"abababbbbaaaabbbbb")#find pattern ab in in that string, matcher is
print(matcher)
cnt=0
for match in matcher:
    print(match.start())#return the first index of ab in thhat string
    print(match.group())#ab
    cnt=cnt+1
print("count of",pattern,"is",cnt)
