class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return

            letters = phone_map[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations

if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))  
    print(solution.letterCombinations(""))    
    print(solution.letterCombinations("2"))
