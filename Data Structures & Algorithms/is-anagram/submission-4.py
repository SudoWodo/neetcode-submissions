class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def buildCounter(s):
            counter = {}
            for letter in s:
                counter[letter] = counter.get(letter, 0) + 1
            return counter

        return buildCounter(s) == buildCounter(t)
        
