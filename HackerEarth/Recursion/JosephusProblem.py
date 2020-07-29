def JosephusProblem(n, k):
	if n == 1:
		return 1
	ret = (JosephusProblem(n-1, k) + k-1) % n+1
	# print(ret, n, k)
	return ret

print(JosephusProblem(7, 3))
print(JosephusProblem(5, 2))
print(JosephusProblem(6, 2))



# n = 6, k = 2 ------> 5
# 
# 		->	1  ->
# 	6				2
# 	^				|
# 	|				v
# 	5				3
# 		<-	4  <-
# 
