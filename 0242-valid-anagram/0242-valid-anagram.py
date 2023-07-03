class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        checkAnagram = True
        
        hashTableS,hashTableT = {}, {}
        
        for i in s:
            if i in hashTableS : 
                hashTableS[i] += 1
            else: hashTableS[i] = 1
         
        for i in t:
            if i in hashTableT : 
                hashTableT[i] += 1
            else: hashTableT[i] = 1
        
      
        checkAnagram = (hashTableT == hashTableS)
        
        
        
        return checkAnagram
              
        