nums= [3,2,2,3]
val=3
class Solution:
    def removeElement():
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k]=nums[i]
                k+=1
        return k
    
''' what i used here is basically a 2 pointer method,
such that i pointer iterates over the array and the k pointer is used to swap elements of the array
such is achieved with another loop within the iterration'''