class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i,j=0,0
        while i<len(nums1) and j <len(nums2):
            if nums1[i]<=nums2[j]:
                merged.append(nums1[i])
                i+=1
            elif nums2[j]<nums1[i]:
                merged.append(nums2[j])
                j+=1
        if i<len(nums1):
            merged.extend(nums1[i:len(nums1)])
        if j<len(nums2):
            merged.extend(nums2[j:len(nums2)])
        if len(merged)%2==1:
            return(merged[(len(merged)//2)])
        elif len(merged)%2==0:
            return((merged[len(merged)//2 - 1] + merged[len(merged)//2]) / 2)

