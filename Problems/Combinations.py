from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        List=[]
        for i in range(1,n+1):
            List.append(i)
        res=combinations(List,k)
        return res
