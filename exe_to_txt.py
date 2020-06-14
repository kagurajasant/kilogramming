import string
import os
with open("1000 Malicious Exe Samples/names.txt",'r') as name_file:
	line=name_file.read()
	name_list=line.split(".exe\n")
	
name_list.pop(-1)
command_name_list=[]
for name in name_list:
	a=name.replace(" ","\\ ").replace("(","\\(").replace(")","\\)")
	command_name_list.append(a)

command="objdump -d 1000\\ Malicious\\ Exe\\ Samples/{0}.exe|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|paste -d '' -s |sed 's/^/\"/'|sed 's/$/\"/g' >> 1000\\ Malicious\\ Exe\\ Samples/TextDump/{0}.txt"
for fname in command_name_list:
	os.system(command.format(fname))