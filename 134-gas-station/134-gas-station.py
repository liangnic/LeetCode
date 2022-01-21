class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        diffsum = 0
        start = 0
        
        for i in range(len(gas)):
            tank += gas[i]-cost[i]
            diffsum += gas[i]-cost[i]
            
            if tank < 0:
                start = i+1
                tank = 0
                
        return start if start < len(gas) and diffsum >= 0 else -1