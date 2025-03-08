class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix=[1]
        suffix=[]

        res=1
        for i in range(0,len(nums)-1):
            res = res * nums[i]
            prefix.append(res)

        res=1
        for i in range(len(nums) - 1, 0, -1):
            res = res * nums[i]
            suffix.append(res)

        suffix.reverse()
        suffix.append(1)

        for i in range(len(nums)):
            nums[i]=prefix[i]*suffix[i]

        return nums