class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        result=0
        curr=0
        for i in range(1,len(values)):
            curr=max(curr,values[i-1]+i-1)
            result=max(result,curr+values[i]-i)
        
        return result