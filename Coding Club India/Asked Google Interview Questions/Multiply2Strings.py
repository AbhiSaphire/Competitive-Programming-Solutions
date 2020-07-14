def Multiply2Strings(s1, s2):
	return str(int(s1) * int(s2))

def Multiply2StringsAlgorithm(str1, str2):
	if((str1[0] == '-' or str2[0] == '-') and (str1[0] != '-' or str2[0] != '-')): 
		print("-", end = '') 
	if(str1[0] == '-' and str2[0] != '-'): 
		str1 = str1[1:] 
	elif(str1[0] != '-' and str2[0] == '-'): 
		str2 = str2[1:] 
	elif(str1[0] == '-' and str2[0] == '-'): 
		str1 = str1[1:] 
		str2 = str2[1:]
		
	len1 = len(str1) 
	len2 = len(str2)
	if len1 == 0 or len2 == 0: 
		return "0"
	result = [0] * (len1 + len2) 
	i_n1 = 0
	i_n2 = 0
	for i in range(len1 - 1, -1, -1): 
		carry = 0
		n1 = ord(str1[i]) - 48
		i_n2 = 0
		for j in range(len2 - 1, -1, -1):  
			n2 = ord(str2[j]) - 48
			summ = n1 * n2 + result[i_n1 + i_n2] + carry  
			carry = summ // 10
			result[i_n1 + i_n2] = summ % 10
			i_n2 += 1
		if (carry > 0): 
			result[i_n1 + i_n2] += carry  
		i_n1 += 1 
	i = len(result) - 1
	while (i >= 0 and result[i] == 0): 
		i -= 1
	if (i == -1): 
		return "0"
	s = "" 
	while (i >= 0): 
		s += chr(result[i] + 48) 
		i -= 1
	return s 

print(Multiply2Strings("456274856234785603716523408756347562384957832465823475827349572389475892347589324758934798278056387456263748652734652873465872365876234875632874657342", "-8723457346578324657342526348923578092475834275834758923745892734868732456728346587346572834658726348575601346573485623478562387456273465347563428756"))
print(Multiply2StringsAlgorithm("456274856234785603716523408756347562384957832465823475827349572389475892347589324758934798278056387456263748652734652873465872365876234875632874657342", "-8723457346578324657342526348923578092475834275834758923745892734868732456728346587346572834658726348575601346573485623478562387456273465347563428756"))
