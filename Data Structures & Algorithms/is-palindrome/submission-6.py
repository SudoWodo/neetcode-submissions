class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char.lower() for char in s if char.isalnum()])

        for idx in range(len(s)):
            if idx > len(s) - idx - 1:
                break
            if s[idx] != s[len(s) - idx - 1]:
                return False
        
        return True