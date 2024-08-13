class Solution(object):
    def mergeArrays(self, nums1, nums2):
        def merge_recursive(i, j):
            if i == len(nums1):
                return nums2[j:]
            if j == len(nums2):
                return nums1[i:]
            
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            
            if id1 == id2:
                return [[id1, val1 + val2]] + merge_recursive(i + 1, j + 1)
            elif id1 < id2:
                return [[id1, val1]] + merge_recursive(i + 1, j)
            else:
                return [[id2, val2]] + merge_recursive(i, j + 1)

        return merge_recursive(0, 0)

def main():
    nums1 = [[1, 2], [2, 3], [4, 5]]
    nums2 = [[2, 4], [3, 1]]

    solution = Solution()
    result = solution.mergeArrays(nums1, nums2)

    print("INPUTS: ", "nums1: ", nums1, "," , "nums2: ", nums2 )
    print("Resultado:", result)


if __name__ == "__main__":
    main()
