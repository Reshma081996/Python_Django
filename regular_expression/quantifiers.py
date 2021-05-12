from re import *
from re import *

#pattern="a+"#any num of a , excluding 0 num of a
#pattern="a*"#any num of a , excluding 0 num of a
#pattern="a?"#check for a in every place
#pattern="a{2}"#taking 2a together
pattern="a{2,4}"#min=2,max=4
matcher=finditer(pattern,"aaaaabaaababbbbaabbbbb")

for match in matcher:
    print(match.start(),"->",match.group())
