class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(temp, n, open, close, current):
            if len(current) == 2*n:
                temp.append(current)
                return
            
            if open < n:backtrack(temp, n, open+1, close, current+"(")
            if close < open:backtrack(temp, n, open, close+1, current+")")
            
        returner = []
        backtrack(returner, n, 0, 0, "")
        return returner
