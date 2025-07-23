class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        counts=[0]*(n+1)
        print(counts)
        

        for i in range(0, n):
            if(citations[i]<= n):
                counts[citations[i]]+=1
            else:
                counts[n]+=1
        print(counts)

        papers=counts[n]
        h=n

        while papers<h:

            h-=1
            papers+=counts[h]
        
        return h




        