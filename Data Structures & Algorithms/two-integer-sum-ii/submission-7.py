class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        memory = dict()
        for idx in range(len(numbers)):
            diff = target - numbers[idx]

            if diff in memory:
                return [memory[diff] + 1, idx + 1]
            else:
                memory[numbers[idx]] = idx
            
