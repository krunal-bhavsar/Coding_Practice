nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
i=0
j=0
for i in range(m, len(nums1)):
    nums1[i]=nums2[j]
    j+=1
    if(j==n):
        break
nums1.sort()
print(nums1)