class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        
        freq_pair = [(v, k) for k,v in counter.items()]
        heap = []

        for pair in freq_pair:
            heapq.heappush(heap, pair)
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for idx in range(k):
            result.append(heapq.heappop(heap)[1])
        return result