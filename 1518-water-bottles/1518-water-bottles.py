class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res=numBottles
        while numBottles>=numExchange:
            consumed=numBottles//numExchange
            stay=numBottles%numExchange
            res+=consumed
            numBottles=consumed+stay
        return res