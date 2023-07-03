
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkCD = True
        setLength  = len(set(nums))
        listLength = len(nums)
        if setLength == listLength:
            checkCD = False      

        return checkCD