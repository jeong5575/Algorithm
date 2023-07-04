from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] +=1
            
            
        temp = sorted(count.items(), key = lambda x:x[1])[-k:]
        return [ x[0] for x  in temp] 
        