def k(i,p,h,c):
    if c<=0:
        return 0
    if h<0:
        return 0
    if dp[h][c]!=-1:
        return dp[h][c]
    o1=0
    if i[h]<=c:    
        o1=k(i,p,h-1,c-i[h])+p[h]  #inlude i[h]
    o2=k(i,p,h-1,c)   # not included i[h]
    dp[h][c]= max(o1,o2)
    return dp[h][c]


item=[10,20,30]
profit=[60,100,120]
c=45
h=len(profit)-1
dp=[[-1 for x in range(c+1)] for y in range(h+1)]
print(k(item,profit,h,c))
