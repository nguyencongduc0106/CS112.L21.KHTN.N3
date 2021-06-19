from collections import defaultdict
def findways():
    visited = [] 
    count = 0
    queue = [(0, -1, a)]
    while queue:
        consumed, pre, ver = queue.pop(0)
        if consumed == k and ver == b:
            count += 1
            continue
        elif consumed > k or (ver == b and consumed != k):
            continue
        else:
            for weigh, nextver in graph[ver]:
                if (pre, ver, next) not in visited:
                    queue.append((weigh + consumed, ver, nextver))
                    visited.append((pre, ver, nextver))
                    
    if (count > 0):
        return count 
    return  -1
n, m = map(int, input().split())
graph = defaultdict(list)
for i in range (m):
  u, v, w = map(int, input().split())
  graph[u].append((w,v))
  graph[v].append((w,u))
a, b, k = map(int, input().split())
rst=findways()-1
print(rst)