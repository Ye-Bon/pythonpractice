import os, re, codecs

f=open("freinds.txt",'r')
script101 = f.read()

character=[x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:',script101)))]
print(character)