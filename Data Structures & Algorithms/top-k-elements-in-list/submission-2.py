class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        frequency_count = [(v, k) for k,v in counter.items()]
        for count, key in frequency_count:
            heapq.heappush(heap, (count, key))
            if  len(heap) > k:
                heapq.heappop(heap)

        result = []
        for pair in heap:
            result.append(pair[1])

        return result