class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charset = set()
        left = 0
        window = 0
        max_window = 0

        for right in range(len(s)):

            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            
            
            charset.add(s[right])
            max_window = max(max_window, right - left + 1)
            # print(f'left : {left}, right: {right}, max_window: {max_window},charset: {charset}')
        
        return max_window

        
