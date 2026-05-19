class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def exec_word_counter(s: str):
            word_counter = {}
            for letter in s:
                word_counter[letter] = word_counter.get(letter, 0) + 1

            return word_counter

        map1 = exec_word_counter(s) 
        map2 = exec_word_counter(t)

        return map1 == map2 