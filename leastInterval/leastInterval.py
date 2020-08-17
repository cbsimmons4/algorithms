class Solution:
    def leastInterval(self, tasks, n):
        tasksCountSort = sorted(tasks, key = tasks.count,reverse = True)
        count = {}
        for task in tasks:
            if task in count:
                count[task] += 1
            else:
                count[task] = 1
        peckingOrder = []
        for num in tasksCountSort:
            if len(peckingOrder) == 0:
                peckingOrder.append(num)
            elif peckingOrder[-1] != num:
                peckingOrder.append(num)
        res = []
        while count[peckingOrder[0]] > 0:
            quota = n+1
            for peck in peckingOrder:
                if quota <= 0: break
                if count[peck] > 0:
                    res.append(peck)
                    count[peck] -= 1
                    quota -= 1
        return res


mySolution = Solution()
print(mySolution.leastInterval(["A","A","A","A","A","A","B","C","D","E","E","E","F","G"], n = 2))




