def ValidateIPv4(s):
	def IPV4(s):
		try: return str(int(s)) == s and 0 <= int(s) <= 255
		except: return False
	        
	if s.count(".") == 3 and all(IPV4(i) for i in s.split(".")):
		return 1
	else:
		return 0

print(ValidateIPv4("277.adf56.564.354"))
print(ValidateIPv4("0.0.0.0"))
print(ValidateIPv4("00.00.00.00"))
print(ValidateIPv4("000.000.000.000"))
print(ValidateIPv4("0000.0000.0000.0000"))

