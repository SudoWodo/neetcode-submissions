class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1

        my_list = list(counter.items())
        my_list.sort(key = lambda x: x[1], reverse = True)

        return [k for k,v in my_list][:k]