from re import *

#predifined character set
#pattern='[ab]'#check for either a or b
#pattern='[a-z]'#will check for lowacase freom ato z
#pattern='[A-Z]'#will check for UPPcase freom ato z
#pattern='[a-zA-Z]'
#Pattern='[0-9]'#check for digits
#pattern='[^0-9]'#except 0to 9
#pattern='[a-zA-Z0-9]'
#pattern='[^a-zA-Z0-9]'

#----------------------------------------------------------------------------------------------------------
#predifined characters
#pattern="\s"#check for spaces
#pattern="\d"#check for digit [0-9]
#pattern="\D"#EXCEPT DIGITS [^0-9]
#pattern="\w" #check for all words [a-za-z0-9_] except specail charcter
pattern="\W" #specail characters exceopt [a-za-z0-9_]
matcher=finditer(pattern,"abc _7ZK@c")
for match in matcher:
    print(match.start(),"->",match.group())
