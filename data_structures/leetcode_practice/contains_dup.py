class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        temp_dict = {}
        for item in nums:
            try:
                temp_val = temp_dict[item]
                return True
            except KeyError:
                temp_dict[item] = True
        return False
    
test = Solution()

print(test.containsDuplicate([1,2,3,1]))
print(test.containsDuplicate([1,2,3,4]))
print(test.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))


########## 583 ms - 33.20% ###############