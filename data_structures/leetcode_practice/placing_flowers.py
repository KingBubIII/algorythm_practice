class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        prev = None
        curr = flowerbed[0]
        next_val = flowerbed[1]
        length = len(flowerbed)
        index = 0

        while (index <= length):
            if (not curr) and not(prev or next_val):
                flowerbed[index] = 1
                n-=1
            
            prev = flowerbed[index-1]
            curr = flowerbed[index]
            next_val = flowerbed[index+1] if index < length-1 else None
            index += 1

        if n > 0:
            return False
        else:
            return True
    
test = Solution()
print(test.canPlaceFlowers([1,0,0,0,1],1))
print(test.canPlaceFlowers([1,0,0,0,1],2))
