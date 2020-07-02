To extract the YARA rules from a family of .exes:
	1) Place them all in a folder (after unzipping if they are in .zip format)
	2) Run the following commands in the same order:
		i) >> python3 preprocessing_kilogramming.py <n-gram length> <relative directory of the .exe files in double quotes>
		ii) >> python3 kilogramming.py <n-gram length> <relative directory of the .exe files in double quotes>
		iii) >> python3 kilogramming_extract.py <n-gram length> <relative directory of the .exe files in double quotes>
		iv) >> python3 create_yara <n-gram length> <relative directory of the .exe files in double quotes>

		For example, on my PC, the python code is present in the directory "Internship", and the malicious family I want to create YARA rules from is in "Internship/family_samples/Malware_Samples_large-20200617T155327Z-001/Malware_Samples_large/Backdoor.WIN32.Gobot.a", where Backdoor.WIN32.Gobot.a is the family name. To create the YARA rules for 1000-grams, you do the following:

		i) >> python3 preprocessing_kilogramming.py 1000 "family_samples/Malware_Samples_large-20200617T155327Z-001/Malware_Samples_large/Backdoor.WIN32.Gobot.a"

		ii) >> python3 kilogramming.py 1000 "family_samples/Malware_Samples_large-20200617T155327Z-001/Malware_Samples_large/Backdoor.WIN32.Gobot.a"

		iii) >> python3 kilogramming_extract.py 1000 "family_samples/Malware_Samples_large-20200617T155327Z-001/Malware_Samples_large/Backdoor.WIN32.Gobot.a"

		iv) >> python3 create_yara 1000 "family_samples/Malware_Samples_large-20200617T155327Z-001/Malware_Samples_large/Backdoor.WIN32.Gobot.a"


	Note 1: These scripts must be run on a POSIX-compliant OS as there are a couple bash commands I have used to process the .exes and files. 
	Note 2: If the preprocessing returns empty .txt files (identifiable by their 1 byte size), the file cannot be tested on the YARA rules.
	Note 3: If there is very low detection, I would try changing the number of strings being searched for in the YARA rules.