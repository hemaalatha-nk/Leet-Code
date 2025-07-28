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