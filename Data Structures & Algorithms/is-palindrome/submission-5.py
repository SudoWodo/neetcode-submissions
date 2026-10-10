class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([char for char in s if char.isalnum()])
        print(s)
        for idx1 in range(len(s)):
            if idx1 > len(s) - idx1:
                break 
            if s[idx1] != s[len(s) - idx1 - 1]:
                return False

        return True 