from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict (list)
        
        
        for s in strs:
            
            anagram["".join(sorted(s))].append(s)
        
        return list(anagram.values())        
        
        