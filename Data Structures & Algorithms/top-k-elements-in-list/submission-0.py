class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        
        top_tuples = [(k,v) for k,v in counter.items()]

        top_tuples.sort(key = lambda x : x[1], reverse = True)
        print(top_tuples)
        return [x[0] for x in top_tuples[:k]]
        