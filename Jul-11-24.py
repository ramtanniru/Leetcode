class Solution:
    def reverseParentheses(self, s: str) -> str:
            stk = []
            for i in s:
                if i!=')':
                    stk.append(i)
                else:
                    temp = ""
                    while stk and stk[-1]!='(':
                        temp += stk.pop()
                    stk.pop()
                    for i in temp:
                        stk.append(i)
            return "".join(stk)