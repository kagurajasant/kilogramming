import kth_largest as kl


def quickselect(score):


	# # 	print(kl.kthlargest(score,i))


	kl_score=[]
	for i in range(1,11):
		kl_score.append(kl.kthlargest(score,i))

	#print(kl_score)

	# for i in range(0,10):
	# 	print(kl_score[i],score[kl_score[i]])
	ret_list=[]

	for i in kl_score:
		ret_list.append(score.index(i))
	return ret_list



# score=[]
# with open("T-list_1000.txt", "r") as f:
# 	for line in f:
# 		score.append(int(line.strip()))
# ret_list=quickselect(score)
# print(ret_list)
