class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = " ".join([char for char in s if ord(char) > ord('A')])
        print(s)
        print(s[::-1])
        return s == s[::-1]