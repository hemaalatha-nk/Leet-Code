class Solution:
    def isHappy(self, n: int) -> bool:

        ans=set()
        temp=n
   
        while True:
            
            output=0
            
            while temp:
                digit=temp%10
                
                digit=digit ** 2
                output+= digit
                print(output)
                temp=temp//10 
                

                
                
            
            # temp=s
            if output==1:
                return True
            temp= output
            if output in ans:
                    return False
            ans.add(output)
            print(temp,ans)
                
            
         
        
        