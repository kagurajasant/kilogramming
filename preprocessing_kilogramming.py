import os
import sys

family_directory=str(sys.argv[1])

if family_directory[-1]!="/":
	family_directory=family_directory+"/"

family_directory_bashformat=family_directory.replace(" ","\\ ").replace("(","\\(").replace(")","\\)")

og_dir=os.getcwd()
os.chdir(family_directory_bashformat)
print("currdir=\n",os.getcwd())

os.system("mkdir -p TextDump")
os.system("ls *.exe > TextDump/names.txt")

with open("TextDump/names.txt",'r') as name_file:
	line=name_file.read()
	name_list=line.split(".exe\n")
name_list.pop(-1)

command_name_list=[]
for name in name_list:
	a=name.replace(" ","\\ ").replace("(","\\(").replace(")","\\)")
	command_name_list.append(a)

command="objdump -d {0}.exe|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|paste -d '' -s |sed 's/^/\"/'|sed 's/$/\"/g' > TextDump/{0}.txt"
for fname in command_name_list:
	os.system(command.format(fname,family_directory_bashformat))
	os.system("sed -i 's/\"//g' TextDump/{0}.txt".format(fname,family_directory_bashformat))
	os.system("sed -i 's/\\n//g' TextDump/{0}.txt".format(fname,family_directory_bashformat))
