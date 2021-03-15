import re

line = "Hoc Python la de hon hoc Java"

matchObj = re.match(r'(.*) la (.*?) .*', line, re.M|re.I)

if matchObj:
	print ("matchObj.group() : "+ matchObj.group())
	print ("matchObj.group(1) : "+ matchObj.group(1))
	print ("matchObj.group(2) : "+ matchObj.group(2))
else:
	print ("Khong co ket noi!")