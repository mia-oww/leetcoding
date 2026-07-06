# Last updated: 7/6/2026, 12:27:36 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        # to find the median, we can do two pointer until it meets in the middle (check even and odd, also if pters out of idnex)
4        # 1. start by combining nums 1 and nums 2 sorted (do using two pter)
5        # 2. then we can do two pointers to meet in the middle, but if odd take middle num if even do midpoint eq
6        
7        p1 = 0 # start of nums1
8        p2 = 0 # start of nums2
9
10        steps = 0
11        
12        midpoint = (len(nums1) + len(nums2)) // 2
13        current = 0
14        while steps <= midpoint: 
15            prev_value = current
16# first checking if pointers within bounds(edge cases)
17            if p1 >= len(nums1):
18                # if our p1 pter out of bounds then our new pter will be based on p2
19                current = nums2[p2] 
20                p2 += 1
21            
22            elif p2 >= len(nums2):
23                # if our p2 pter out of bounds then new pter is p1 
24                current = nums1[p1]
25                p1 += 1
26            
27            elif nums1[p1] < nums2[p2]: # check which is the smallest number, that will be current in array
28                current = nums1[p1]
29                p1 += 1
30            else:
31                current = nums2[p2]
32                p2+= 1
33            
34            steps +=1
35
36#now have to check odd vs even length
37        total_len = len(nums1) + len(nums2)
38        if total_len % 2 != 0:
39            return float(current) # returns middle num if odd 
40        else:
41            return (prev_value + current) / 2.0 # returns avg of even array, (2+3)/2 = 2.5
42
43            
44