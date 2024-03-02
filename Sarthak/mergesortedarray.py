class Solution:
    nums1 = [1,2,3,0,0,0] 
    m = 3
    nums2 = [2,5,6] 
    n = 3
    def merge(nums1, m, nums2, n):
        z=0
        for element in range(z,n):
            nums1[m]= nums2[z]
            z+=1
            m+=1
        nums1.sort()
