from typing import List
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged = {}
        for id_, val in nums1:
            merged[id_] = merged.get(id_, 0) + val
        for id_, val in nums2:
            merged[id_] = merged.get(id_, 0) + val        
        return sorted([[id_, val] for id_, val in merged.items()])
Value_Sum = Solution()
print(Value_Sum.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))  
print(Value_Sum.mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))
