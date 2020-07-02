import sys
import rolling_hash as rh
import os


n=int(sys.argv[1])
number_of_hashes=int(sys.argv[3])
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

T=[]
with open("TextDump/T-list_{0}.txt".format(str(n)), "r") as f:
	for line in f:
		T.append(int(line.strip()))

x=[]
for i in T:
	x.append(i)

T.sort()
largest_hash=T[-number_of_hashes:]
hash_val_list=[]
print(largest_hash)

for i in largest_hash:
	hash_val_list.append(x.index(i))
	x[x.index(i)]=0		


S=[]
counter=0
for fname in name_list:
	with open("TextDump/{0}.txt".format(fname),'r') as f:
		text=f.read()

	token=text.split()
	S=rh.iterated_check(S,token,n,hash_val_list)
	counter=counter+1
	print("done with file {0}, progress={1}/{2}".format(fname,counter,str(len(name_list))))



listf=open("TextDump/S-list_{0}.txt".format(str(n)),"w")
for i in S:
	listf.write(str(i)+'\n')
listf.close()
