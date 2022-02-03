import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr=nums1+nums2;
        n=len(arr);
        arr.sort();
        if n%2==0:
            return (arr[(n-2)/2] + arr[n/2])/2.0;
        else:
            return arr[n/2];
