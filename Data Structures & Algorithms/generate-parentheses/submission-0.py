class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # so we go down two paths 
        # we either pick the ( or we pick ) 
        # we pick it within specific constraints
        # we can pick an open ( parentheses if the current number of 
        # open parentheses is less than the n. 
        # we can pick close only if the current open is greater than close
        # so that there is actually something to close. 

        res, sol = [], []

        def backtrack(open, close):
            if len(sol) == 2*n:
                res.append("".join(sol))

            if open < n: 
                sol.append("(")
                backtrack(open+1, close)
                sol.pop()

            if open > close:
                sol.append(")")
                backtrack(open, close+1)
                sol.pop()
            
        backtrack(0, 0)
        return res
