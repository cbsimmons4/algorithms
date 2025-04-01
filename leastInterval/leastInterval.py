from collections import Counter
from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks, n):
        # Count the frequency of each task
        task_counts = Counter(tasks)
        # Use a max heap to store the negative of task counts (to simulate max heap in Python)
        max_heap = [-count for count in task_counts.values()]
        heappush(max_heap, 0)  # Push a dummy value to avoid empty heap issues

        time = 0
        while max_heap:
            cooldown = []
            # Process up to n+1 tasks in one cycle
            for _ in range(n + 1):
                if max_heap:
                    count = heappop(max_heap)
                    # If the task still has remaining instances, add it to cooldown
                    if count < -1:
                        cooldown.append(count + 1)
                time += 1
                # Break early if no tasks are left to process
                if not max_heap and not cooldown:
                    break
            # Push tasks from cooldown back into the heap
            for task in cooldown:
                heappush(max_heap, task)
        return time


mySolution = Solution()
print(mySolution.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "E", "E", "F", "G"], n=2))




