class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left_p=0
        right_p=len(numbers)-1
        while right_p>left_p:
            s=numbers[right_p]+numbers[left_p]
            if(s==target):
                return[left_p+1,right_p+1]
            elif(s>target):
                right_p-=1
            else:
                left_p+=1
        return False




        right_p= len(numbers)-1
        if(right_p==1 and numbers[0]+numbers[1]==target):
            return [1,2]
        
        left_p= 0
        mid_p=len(numbers)/2-1
        n=right_p

        for i in range(0, len(numbers)):
            left_p=i+1
            right_p= len(numbers)-1
            mid_p=int((left_p+2+right_p)/2)-1

            while right_p >= left_p:

                diffs=target-numbers[i]
                if( diffs==numbers[mid_p]):
                    return [1+i, 1+mid_p]
                elif (diffs>numbers[mid_p]):
                    left_p=mid_p+1
                    mid_p=int((left_p+2+right_p)/2)-1
                else:
                    right_p=mid_p-1
                    mid_p=int((left_p+2+right_p)/2)-1
        return False






        