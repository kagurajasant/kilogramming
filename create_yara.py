import os
import sys


n=int(sys.argv[1])
family_directory=str(sys.argv[2])

if family_directory[-1]!="/":
	family_directory=family_directory+"/"

family_directory_bashformat=family_directory.replace(" ","\\ ").replace("(","\\(").replace(")","\\)")

os.chdir(family_directory_bashformat)
print("current directory=\n",os.getcwd())


with open("TextDump/S-list_{0}.txt".format(str(n)),'r') as f:
	pf_text=f.read()

f_text=pf_text.replace("[","").replace("]","")

all_strings=f_text.split("\n")

yara_rule_file=open("TextDump/yara_rule_{0}.yar".format(str(n)),'w')
yara_rule_file.write("rule Banker\n{\n\tstrings:\n")
rule_counter=0
for string in all_strings:
	a_list=string.split(", ")
	if a_list[-1]=="":
		a_list.pop(-1)

	a=''
	for i in a_list:
		a=a+hex(int(i))[2:].zfill(2)+" "
	if a!="":
		yara_rule_file.write("\t\t$r{0}=\"{1}\"\n\n".format(str(rule_counter),a[:-1]))
	rule_counter=rule_counter+1

#yara_rule_file.write("\n\tcondition:\n\t\t{0} of ($r*)\n}}".format(int(0.1*rule_counter)))
yara_rule_file.write("\n\tcondition:\n\t\t{0} of ($r*)\n}}".format(int(1)))
yara_rule_file.close()