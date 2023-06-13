class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        highest = max(candies)
        ret = []
        for kid in candies:
            ret.append(True if kid+extraCandies >= highest else False)
        print(ret)


test = Solution()
res1 = test.kidsWithCandies([2,3,5,1,3], 3)
res2 = test.kidsWithCandies([4,2,1,1,2], 1)
res3 = test.kidsWithCandies([12,1,12], 10)