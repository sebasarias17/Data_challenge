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
        
        while i < len(nums1):
            result.append(nums1[i])
            i += 1

        while j < len(nums2):
            result.append(nums2[j])
            j += 1

        return result

def main():
    print("Ejecutando main()...")  # Para verificar que se ejecuta
    nums1 = [[1, 2], [2, 3], [4, 5]]
    nums2 = [[2, 4], [3, 1]]

    solution = Solution()
    result = solution.mergeArrays(nums1, nums2)

    print("INPUTS: ", "nums1: ", nums1, "," , "nums2: ", nums2 )
    print("Resultado:", result)


if __name__ == "__main__":
    main()
        