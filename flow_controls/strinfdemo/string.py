#string is a sequence of chracters
#repesent
n="hello"
print(n)
h='hello world'
print(n)
#multiline string use """
name="""hai, helo  
        kakkanad       """
print(name)

#spilt- split string
name="Luminar technolab kakkaknad"
splitii=name.split(" ")
print(splitii)

#upper and lower
name="Luminar technolab kakkaknad"
words=name.upper()
print(words)
lowest=words.lower()
print(lowest)

#remove character from begining -lstrip
name="TTluminarTechnolab"
print(name.lstrip("TT"))
#remove character from end -rstrip
name="luminarTechnolabRR"
print(name.rstrip("RR"))

name="TTTTTTarTechnolab"
print(name.lstrip("TT"))