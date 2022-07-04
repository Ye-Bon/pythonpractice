import os, re, codecs

f=open("freinds.txt",'r')
script101 = f.read()
line = re.findall(r'Monica:.+', script101)
print (line)
f.close()

f= open ("monica.txt",'w')
monica = ''
for i in line:
    monica+=i +'\n'
f.write(monica)
f.close()