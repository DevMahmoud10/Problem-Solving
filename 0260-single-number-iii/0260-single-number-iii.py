class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for n in nums:
            xor^=n
            
        diff_bit=1
        while xor&diff_bit==0:
            diff_bit<<=1
            
        a,b=0,0  
        for n in nums:
            if n&diff_bit==0:
                a^=n
            else:
                b^=n
        return [a,b]