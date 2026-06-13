class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def create_vector(string):
            vec = [0] * 26
            for character in string:
                vec[ord(character) - ord('a')] += 1
            
            return tuple(vec)
        
        look_up = defaultdict(list)
        for string in strs:
            vector = create_vector(string)
            if vector in look_up:
                look_up[vector].extend([string])
            else:
                look_up[vector] = [string]

        result = []
        for _ , value in look_up.items():
            result.append(value)
        
        return result