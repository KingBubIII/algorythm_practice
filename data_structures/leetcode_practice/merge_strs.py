class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        merged = '{}'.join(word1) # O(n)
        if word2_len > word1_len or word1_len == word2_len:
            merged += "{}"*(word2_len-word1_len+1)
        else:
            index = 3*word2_len
            merged = merged[:index] + merged[index:].replace("{}","")
        
        merged = merged.format(*word2)

        return merged
    

test = Solution()
res1 = test.mergeAlternately("abc","pqr")
res2 = test.mergeAlternately("ab","pqrs")
res3 = test.mergeAlternately("abcd","pq")
print(res1)
print(res2)
print(res3)