class Solution:
    def candy(self, ratings: List[int]) -> int:

        no_candy= [1]* len(ratings)

        for i in range(0, len(ratings)-1):
            if(ratings[i]<ratings[i+1]):
                no_candy[i+1]=  no_candy[i]+1

        # print(no_candy)
        for j in range(len(ratings)-1,0,-1):
            # print(j)
            if(ratings[j]<ratings[j-1]):
                no_candy[j-1]= max( no_candy[j-1], no_candy[j]+1)

        
        # print(no_candy)

        return sum(no_candy)
        

        