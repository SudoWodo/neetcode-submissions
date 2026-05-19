class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dsf(n_start, n_close, string):
            # Base Case

            if n_start == n and n_close == n:
                result.append(string)
                return 
            
            # choose "("
            if n > n_start:
                dsf(n_start + 1, n_close, string + "(")
            
            # choose ")"
            if n_start > n_close:
                dsf(n_start, n_close + 1, string + ")")
        
        dsf(0,0,"")

        return result

            