class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def createVector(string: str) -> Tuple[int]:
            vector = [0] * 26
            for letter in string:
                vector[ord(letter) - ord('a')] += 1
            
            return tuple(vector)

        vector_map = {}
        for string in strs:
            vector_tuple = createVector(string)
            if vector_tuple in vector_map:
                vector_map[vector_tuple].append(string)
            else:
                vector_map[vector_tuple] = [string]
        
        return [v for _, v in vector_map.items() ]



