class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        right_p= len(numbers)-1
        if(right_p==1 and numbers[0]+numbers[1]==target):
            return [1,2]
        
        left_p= 0
        mid_p=len(numbers)/2


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






        