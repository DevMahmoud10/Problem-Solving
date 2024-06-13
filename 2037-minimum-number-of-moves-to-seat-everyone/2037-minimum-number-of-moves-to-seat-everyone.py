class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = max(max(seats), max(students)) + 1
        count_seats = [0]*n
        count_students = [0]*n

        for s in seats:
            count_seats[s]+=1
        for s in students:
            count_students[s]+=1

        i,j = 0,0
        res = 0
        remain = len(students)
        while remain:
            if count_seats[i] == 0:
                i+=1
            if count_students[j] == 0:
                j+=1
            if count_seats[i] and count_students[j]:
                res += abs(i-j)
                count_seats[i] -= 1
                count_students[j] -= 1
                remain -= 1
        return res