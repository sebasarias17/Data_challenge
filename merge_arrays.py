class Solution(object):
    def mergeArrays(self, nums1, nums2):
        i,j = 0,0
        result = []
        
        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            if id1 == id2:
                result.append([id1, val1 + val2])
                i +=1
                j +=1
            elif id1 < id2:
                result.append([id1, val1])
                i +=1
            else:
                result.append([id2, val2])
                j +=1

        result.extend(nums1[i:])
        result.extend(nums2[j:])

        return result