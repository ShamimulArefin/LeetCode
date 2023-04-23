# way 1
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        time = arrivalTime + delayedTime
        if time>=24:
            return time-24
        else:
            return time
        
# way 2
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24