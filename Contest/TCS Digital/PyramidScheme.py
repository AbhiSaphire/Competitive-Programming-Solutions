def solve(incentive, percent, remain, n, level):
	if (percent//100)*incentive >= remain:
		return n

	maxnode = (2**level)-1
	if (percent//100)*incentive * maxnode < remain:
		remain = remain - ((percent//100)*incentive * maxnode)
		incentive //= percent
		solve()

incentive = int(input())
percent = int(input())
goal = int(input())
remain = goal-incentive
print(solve(incentive, percent, remain, 0, 2))