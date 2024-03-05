nums = [1,1,1,2,2,3]
class Solution:
    def removeDuplicates():
        counts= {}
        for element in nums:
            if element in counts:
                counts[element] +=1
            else:
                counts[element]=1
        i=0
        while(i<len(nums)):
            if counts[nums[i]]>2:
                counts[nums[i]] -=1
                del nums[i]
            else:
                i+=1