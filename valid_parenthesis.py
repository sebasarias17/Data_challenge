class Solution(object):
    def longestValidParentheses(self, s):
        arr = [*s]
        counter = 0
        arr2 = []
        
        while counter < len(arr):
            if arr[counter] == '(':
                if counter + 1 < len(arr) and arr[counter + 1] == ')':
                    arr2.append(arr[counter])  # Añade '('
                    arr2.append(arr[counter + 1])  # Añade ')'
                    counter += 2  # Salta la pareja de paréntesis
                else:
                    counter += 1  # Si no hay un ')' siguiente, solo avanza
            else:
                counter += 1  # Si no es '(', solo avanza
        
        max_length = len(arr2)  
        print("arreglo original:", arr)
        print("arreglo nuevo:", arr2)
        return max_length
    
def main():
    s = "(()())" 
    solution = Solution()
    result = solution.longestValidParentheses(s)
    print("Resultado:", result)


if __name__ == "__main__":
    main()
