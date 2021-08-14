# The priority queues can be implemented by heaps i.max heap ii.min heap

import heapq
li = [1,20,40,2,3,4,5,6]
heapq.heapify(li)
print(li)
heapq.heappop(li)
print(li)
heapq.heappushpop(li,30)
print(li)