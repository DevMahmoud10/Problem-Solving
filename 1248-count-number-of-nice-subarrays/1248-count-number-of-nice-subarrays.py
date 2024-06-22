class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds,res=0,0
        l,m=0,0
        
        for r in range(len(nums)):
            if nums[r]%2==1:
                odds+=1
                
            while odds>k:
                if nums[l]%2==1:
                    odds-=1
                l+=1
                m=l
                
            if odds==k:
                while nums[m]%2==0:
                    m+=1
                res+=m-l+1
        return res
            
            
            