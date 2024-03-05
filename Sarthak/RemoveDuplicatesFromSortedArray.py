nums=[1,1,2]
class Solution:
    def removeDuplicates():
        k=0
        for i in range(len(nums)):
            if nums[i]!=nums[k]:
                k+=1
                nums[k]=nums[i]
        del nums[k+1:]