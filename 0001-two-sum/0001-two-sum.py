class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashtable = {}
        index = 0
        for i in nums:
            hashtable[i]= index
            index += 1
            
        for i in range(len(nums)):
            if target-nums[i] in hashtable:
                if i != hashtable[target-nums[i]]:
                       return i , hashtable[target-nums[i]]
        
        return [i,hashtable[i]]
        
        
        