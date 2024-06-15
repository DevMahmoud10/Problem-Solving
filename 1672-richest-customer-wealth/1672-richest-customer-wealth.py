class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        for customer in accounts:
            wealth=sum(customer)
            max_wealth=max(wealth,max_wealth)
        return max_wealth