def rh_core(prevhash,l,prevval):
	k=len(l)
	#print("core:",l)
	
	b=10 
	if prevhash==-1 and prevval==-1:
		hval=0
		for i in range(k):
			hval=hval+l[i]*(b**i)
			#print("hval,i=",hval,i)
	
	else:
		hval=((prevhash-prevval)//b)+l[-1]*(b**(k-1))
		#print("hval=",hval)	
	
	return (int(hval),l[0])



def iterator_rh(str_token_list,n,T):
	m=1020379 #large prime 0xffffff=16,777,215	
	# T=[0]*m
	token_list=[int(i,16) for i in str_token_list]
	prevval=0
	prevhash=0
	k=len(token_list)
	for i in range(0,k):
		if i+n<=k:
			l=token_list[i:i+n]
			#print("iterator:",l)
			if i==0:
				prevhash=-1
				prevval=-1
			(prevhash,prevval)=rh_core(prevhash,l,prevval)
			hashmod=prevhash%m
			#print("hvalmod=",hashmod)	
			T[hashmod]=T[hashmod]+1
			#print("\n\n")
			#print (prevhash,prevval,T[prevhash],'\n')
			#print ("iterator:prevhash,prevval,hashmod,T[hashmod]=",prevhash,prevval,hashmod,T[hashmod],'\n')
	return T	



def iterated_check(S,str_token_list,n,hash_val_list):
	m=1020379 #large prime 0xffffff=16,777,215	
	# T=[0]*m
	#print("rolling hash:",hash_val_list)
	token_list=[int(i,16) for i in str_token_list]
	
	prevval=0
	prevhash=0
	k=len(token_list)
	for i in range(0,k):
		if i+n<=k:
			l=token_list[i:i+n]
			#print("iterator:",l)
			if i==0:
				prevhash=-1
				prevval=-1
			(prevhash,prevval)=rh_core(prevhash,l,prevval)
			hashmod=prevhash%m
			#print("hvalmod=",hashmod)	
			if hashmod in hash_val_list:
				#print("l")
				if str(l) not in S:
					S.append(str(l))
	return S
		











# m=541 #large prime 0xffffff=16,777,215	
# T=[0]*m
# print("lol")
# l=["ff","08","45","65","ba","08","45","65","12","08","45","65","ba"]
# #l=["1","2","3","1","2","3"]
# T=iterator_rh(l,4,T)
