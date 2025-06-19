class Solution:
    def reverse(self, x: int) -> int:
            res=0
            temp_x=x
            if((x< -2 ** 31 ) or( x> ((2 ** 31) -1))):
                return 0
            while temp_x!=0:
                print(temp_x)
                print((res*10) , (temp_x%10))
                if(temp_x>0):
                    res=(res*10) + (temp_x%10)
                else:
                    res=(res*10) + (temp_x%-10)
                temp_x=int(temp_x/10)
            if((res< -2 ** 31 ) or( res>(( 2 ** 31) -1))):
                return 0
            return res
        