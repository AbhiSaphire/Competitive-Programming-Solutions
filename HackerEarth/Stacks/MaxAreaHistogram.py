'''
Function Arguments :
		@param  : histogram( given list containing info about histogram)
		@return : integer
'''

def getMaxArea(hist):
    stack = []
    max_area = -1
    i = 0
    while i < len(hist):
        if not stack or hist[stack[-1]] < hist[i]:
            stack.append(i)
            i += 1
        else:
            y = stack.pop()
            area = hist[y] * ((i - stack[-1]-1) if stack else i)
            max_area = max(max_area, area)
    
    while stack:
        y = stack.pop()
        area = hist[y] * ((i - stack[-1]-1) if stack else i)
        max_area = max(max_area, area)
    
    return max_area

print(getMaxArea([3, 2, 4, 3, 2, 1, 10, 2, 2, 2, 2, 5, 4, 5, 3, 5, 10]))