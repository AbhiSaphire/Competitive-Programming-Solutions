from math import floor, log

def return_step_count(n, dic):
	if n in dic:
		return dic[n]
	else:
		if n&1:
			dic[n] = min(return_step_count((n+1)>>1, dic)+2, return_step_count((n-1)>>1, dic)+2)
		else:
			dic[n] = return_step_count(n>>1, dic)+1
	return dic[n]

def solution(n):
	returner = 0
	dic = {1: 0}
	n = int(n)
	returner = return_step_count(n, dic)	
	return returner

print(solution('4'))
print(solution('5'))
print(solution('15'))
print(solution('6'))
print(solution('3487328597234534257287'))
print(solution('673672894772904000435345366848646854454846168413745683574865147158531862352346536545465756454647557577763'))
