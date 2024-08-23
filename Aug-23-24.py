class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a,b):
            while b:
                a,b = b,a%b
            return abs(a)
        if not expression:
            return '0/1'
        flag = True
        temp = ""
        fractions = []
        for i in expression:
            if i=='+' or i=='-':
                if temp:
                    if flag:
                        fractions.append(temp)
                    else:
                        fractions.append('-'+temp)
                if i=='+':
                    flag = True
                else:
                    flag = False
                temp = ""
            else:
                temp += i
        if flag:
            fractions.append(temp)
        else:
            fractions.append('-'+temp)
        
        numerator = 0
        denominator = 1

        for i in fractions:
            num,den = map(int,i.split('/'))
            numerator = numerator*den + num*denominator
            denominator *= den
        common = gcd(numerator,denominator)
        numerator //= common
        denominator //= common
        return str(numerator)+'/'+str(denominator) 