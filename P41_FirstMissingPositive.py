#41 First Missing positive
'''Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a=set(nums)
        i=1
        while i in a:
            i+=1
        return i
        
