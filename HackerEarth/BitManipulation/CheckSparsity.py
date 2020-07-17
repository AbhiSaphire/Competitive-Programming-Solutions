def CheckSparsity(n):
	return True if n & (n >> 1) == 0 else False


print(CheckSparsity(72))
print(CheckSparsity(2))
print(CheckSparsity(3))

# 72 		-->	01001000
# n >> 1 	-->	00100100
# 				--------
# 				00000000	<-- True

# 2			-->	10
# n >> 1	-->	01
# 				--
# 				00			<-- True

# 3			-->	11
# n >> 1	-->	01
# 				--
# 				01			<-- False