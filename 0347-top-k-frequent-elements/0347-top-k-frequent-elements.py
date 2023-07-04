
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] +=1
            

        return [ x[0] for x  in sorted(count.items(), key = lambda x:x[1])[-k:]] 
        