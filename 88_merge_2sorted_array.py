nums1=[2,0]
m=1
nums2=[1]
n=1
place=m+n-1

while m>0 and n>0:
    if nums2[n-1]>nums1[m-1]:
        nums1[place]=nums2[n-1]
        n=n-1
    else:
        nums1[place]=nums1[m-1]
        m=m-1
    place=place-1
#n=1 p=0 m=0
if m<=0:#n!=0
    nums1[:n]=nums2[:n]
print(nums1)
