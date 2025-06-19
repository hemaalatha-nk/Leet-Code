class Solution:
    def reverse(self, x: int) -> int:
        min_x= -2 ** 31 
        max_x=(2 ** 31) -1
        res=0
        if((x< min_x ) or( x> max_x)):
            return 0
        if(x<0):
            x=x*-1
            sx=f"{x}"
            res=int(sx[::-1]) * -1
        else:
            sx=f"{x}"
            res=int(sx[::-1])
        if((res< min_x ) or( res>max_x)):
                return 0
        return res
            # res=0
            # temp_x=x
            # min_x= -2 ** 31 
            # max_x=(2 ** 31) -1
            # if((x< min_x ) or( x> max_x)):
            #     return 0
            # while temp_x!=0:
            #     if(temp_x>0):
            #         res=(res*10) + (temp_x%10)
            #     else:
            #         res=(res*10) + (temp_x%-10)
            #     temp_x=int(temp_x/10)
            # if((res< min_x ) or( res>max_x)):
            #     return 0
            # return res
        