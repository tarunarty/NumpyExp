import sys
  
# Returns cost of minimum cost path from (0,0) to (m, n) in mat[R][C] 
def minCost(cost, m, n): 
    if (n < 0 or m < 0): 
        return sys.maxsize 
    elif (m == 0 and n == 0): 
        return cost[m][n] 
    else: 
        return cost[m][n] + min( minCost(cost, m-1, n-1), 
                                minCost(cost, m-1, n), 
                                minCost(cost, m, n-1) ) 
 
# Driver program to test above functions  
cost = eval(input())
print(minCost(cost, 2, 2))
