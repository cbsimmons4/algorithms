class Solution:
    def topKFrequent(self, nums, k):
        bucketCountMap = {}
        for num in nums:
            if num not in bucketCountMap.keys():
                bucketCountMap[num] = 1
            else:
                bucketCountMap[num] += 1

        bucketNumsMap = {}
        for cur in bucketCountMap.keys():
            if  bucketCountMap[cur] not in bucketNumsMap.keys():
                bucketNumsMap[bucketCountMap[cur]] = [cur]
            else:
                 bucketNumsMap[bucketCountMap[cur]].append(cur)
                 
        res = []
        quota = k

        for cur in sorted(bucketNumsMap.keys(),reverse=True):
            if (quota <= 0 ): break
            for num in bucketNumsMap[cur]:
                if quota <= 0: break
                res.append(num)
                quota -= 1    
        return res


mySolution = Solution()
print(mySolution.topKFrequent([1,2,3,1,5,2],2))