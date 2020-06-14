def rh_core(prevhash,l,prevval):
	k=len(l)
	m=1,299,709 #large prime 0xffffff=16,777,215
	b=10
	if prevhash==-1 and prevval==-1:
		hval=0
		for i in range(k):
			hval=hval+l[i]*(b**i)
	
	else:
		hval=(prevhash-prevval)/b+l[-1]*(b**(k-1))
	hval=hval%m		
	return (hval,l[0])



def iterator_rh(token_list,n):
	prevval=0
	prevhash=0
	k=len(token_list)
	# while k%n!=0:
	# 	token_list.append(0)
	for i in range(0,k):
		if i+n<=k:
			l=token_list[i:i+n]
			print(l)
			if i==0:
				prevhash=-1
				prevval=-1
			(prevhash,prevval)=rh_core(prevhash,l,prevval)
			print (prevhash,prevval,'\n')

		


# l=[1,2,3,4,1,2,3]
# print(rh_core(-1,l,-1))
# iterator_rh(l,3)