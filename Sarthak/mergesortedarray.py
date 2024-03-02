nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

def merge(self, nums1, m , nums2, n) -> None:
        p=m-1
        q=n-1
        z=0
        i=m+n-1
        for element in range(z,n):
            nums1[m]= nums2[z]
            p+=1
            z+=1
            m+=1
        nums1.sort()
        print(nums1)

        """
        Do not return anything, modify nums1 in-place instead.
        """
        