class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        givenSum,expSum=sum(nums),int(n*(n+1)/2)
        return expSum-givenSum
