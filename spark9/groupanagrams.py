class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):    
        a_dict=dict()
        j=1
        for i in range(len(strs)):
            temp=''.join(sorted(strs[i]))
            if temp not in a_dict:
                j=1
                a_dict[temp]=[strs[i]]
            else:
                j+=1
                a_dict[temp].append(strs[i])
        a_list=list(a_dict.values())
        return a_list
    
strs=["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))