from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        
        for row in image:
            for i in range((n + 1) // 2):
                row[i], row[n - 1 - i] = row[n - 1 - i] ^ 1, row[i] ^ 1
        return image

flip_image = Solution()
print(flip_image.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(flip_image.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
