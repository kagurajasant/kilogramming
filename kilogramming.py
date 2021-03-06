import sys
import rolling_hash as rh
import os

n=int(sys.argv[1])
family_directory=str(sys.argv[2])

if family_directory[-1]!="/":
	family_directory=family_directory+"/"

family_directory_bashformat=family_directory.replace(" ","\\ ").replace("(","\\(").replace(")","\\)")
os.chdir(family_directory_bashformat)
print("current directory=\n",os.getcwd())
with open("TextDump/names.txt",'r') as name_file:
	line=name_file.read()
	name_list=line.split(".exe\n")

name_list.pop(-1)

T=[0]*15485863
counter=0

for fname in name_list:
	with open("TextDump/{0}.txt".format(fname),'r') as f:
		text=f.read()
	token=text.split()
	T=rh.iterator_rh(token,n,T)
	counter=counter+1
	print("done with file {0}, progress={1}/{2}".format(fname,counter,str(len(name_list))))


listf=open("TextDump/T-list_{0}.txt".format(str(n)),'w')
for i in T:
	listf.write(str(i)+'\n')
listf.close()
	



