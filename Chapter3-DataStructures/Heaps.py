''' 
What are Heaps?
'''

import heapq
# Define Heap
heap = []

numbers = [3,4,7,1,2]

heapq.heapify(numbers)

print(numbers)
print()

# Heap Methods

# 1. heapq.heappush(heaplist, item)
print("heappush")
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print(heap)
print()

# 2. heapq.heappop(heaplist)
print("heappop") 
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

result = heapq.heappop(heap)
result = heapq.heappop(heap)
print(result)
print()

# 3. heapq.heapify(heaplist)
print("heapify") 
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 80)

heapq.heapify(heap)

print(heap)
print()

# 4. heapq.heappushpop(heaplist, item) 
print("heappushpop") 
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 80)

res = heapq.heappushpop(heap, 0)
print(res)
print()

# 5. heapq.heapreplace(heaplist, item) 
print("heapreplace") 
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 80)

res = heapq.heapreplace(heap, 0)

print(res)
print(heap)
print()

# 6. heapq.nlargest(n, heaplist, key = fn)
print("nlargest") 
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 80)

res = heapq.nlargest(3, heap)
print(res)
print()

# 7. heapq.nsmallest(n, heaplist, key = fn)
print("nsmallest") 
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 80)

res = heapq.nsmallest(3, heap)
print(res)