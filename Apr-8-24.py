class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        a = Counter(students)
        stk = sandwiches
        print(a)
        while(len(stk)!=0 and a[stk[0]]!=0):
            a[stk[0]] -= 1
            stk.pop(0)
        return len(stk)