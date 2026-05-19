class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convertToVec(word: str) -> tuple:
            vec = [0] * 26
            for letter in word:
                vec[ord(letter) - ord('a')] += 1
            
            return tuple(vec)

        vectorStore = {}
        for string in strs:
            stringVec = convertToVec(string)
            if stringVec in vectorStore:
                vectorStore[stringVec].append(string)
            else:
                vectorStore[stringVec] = [string]

        result_list = []
        for key, value in vectorStore.items():
            result_list.append(value)

        return result_list


        