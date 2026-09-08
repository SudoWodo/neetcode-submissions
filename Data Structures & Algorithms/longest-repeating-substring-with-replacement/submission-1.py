class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # naive solution
        answer = 0
        
        for left in range(len(s)):
            count = {}
            for right in range(left, len(s)):
                
                count[s[right]] = count.get(s[right], 0) + 1

                max_freq = max(count.values())
                replacements = right - left + 1 - (max_freq)

                if replacements <= k:
                    answer = max(answer, right - left + 1)
        
        return answer