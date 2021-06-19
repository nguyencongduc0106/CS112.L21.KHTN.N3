def findbestsum(n, sum, memo ={}):
    if sum in memo:
      return memo[sum]
    if sum==0:
      return []
    if sum<0 or n == 0:
      return None
    min = None
    remain = sum - a[n-1]
    s1 = findbestsum(n-1, remain) 
    s2 = findbestsum(n-1, sum)
    if s1!= None:
        cur = [a[n-1]]+s1
        if min == None or len(min) > len(cur):
             min = cur
    if s2!= None:
        able = s2
        if min == None or len(min) > len(cur):
            min = cur
    if min!=None:
        memo[sum] = min
    return min

a = list(map(int,input().split()))
b = int(input())
res = BestSum(len(a), b)
print(res)