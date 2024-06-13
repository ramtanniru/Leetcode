class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        for i,j in zip(seats,students):
            res += abs(i-j)
        return res