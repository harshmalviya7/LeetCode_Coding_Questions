# 733. Flood Fill
# https://leetcode.com/problems/flood-fill/


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        if image[sr][sc ]= =newColor:
            return image


        def image1(image ,sr ,sc ,color ,newColor):
            if (s r <0 or s r> =len(image) or s c <0 or s c> =len(image[0]) or image[sr][sc ]! =color):
                return

            image[sr][sc ] =newColor
            image1(image ,s r +1 ,sc ,color ,newColor)
            image1(image ,s r -1 ,sc ,color ,newColor)
            image1(image ,sr ,s c +1 ,color ,newColor)
            image1(image ,sr ,s c -1 ,color ,newColor)



        image1(image ,sr ,sc ,image[sr][sc] ,newColor)
        return image
