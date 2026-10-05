class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        task_heap = [-n for n in count.values()]
        heapq.heapify(task_heap)
        q = deque() # (-cnt, idleTime)
        time = 0
        while task_heap or q:
            time += 1
            if not task_heap:
                time = q[0][1]
            else:
                t_cnt = heapq.heappop(task_heap)
                if abs(t_cnt) > 1:
                    q.append((t_cnt + 1, time + n))
            if q and q[0][1] == time:
                heapq.heappush(task_heap, q.popleft()[0])
        return time
