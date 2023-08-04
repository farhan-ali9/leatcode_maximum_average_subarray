class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum=sum(nums[:k])
        curt_sum=max_sum
        for i in range(k,len(nums)):
            curt_sum+=nums[i]-nums[i-k]
            max_sum=max(max_sum,curt_sum)
        return max_sum/float(k)
