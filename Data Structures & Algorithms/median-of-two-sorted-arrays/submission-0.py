class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # median of two sorted arrays in O(log(m+n)) time
        # use binary search on the smaller arr and 
        # compare the max elem of left sorted arr
        #with the min elem of right sorted arr
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        left = 0
        right = len(A) - 1

        # start BS
        while True:
            amid = (left + right) // 2
            bmid = half - amid - 2 # make it the same size as A

            # manage out of bounds
            Aleft = A[amid] if amid >= 0 else float("-inf")
            Aright = A[amid + 1] if (amid + 1) < len(A) else float("inf")

            Bleft = B[bmid] if bmid >= 0 else float("-inf")
            Bright = B[bmid + 1] if (bmid + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                #even
                else:
                    return (max(Aleft, Bleft) + min (Aright, Bright)) / 2
            elif Aleft > Bleft:
                # move the right
                right = amid - 1
            else:
                left = amid + 1            



