class Solution:
    def numberToWords(self, num: int) -> str:
        def splitNum(num,l=[]):
            i,cnt,temp = len(num)-1,0,""
            while i>=0:
                if cnt==3:
                    l.append(temp[::-1])
                    temp = num[i]
                    cnt = 1
                    i -= 1
                    continue
                temp += num[i]
                cnt += 1
                i -= 1
            l.append(temp[::-1])
            return l
        def numToString(s):
            res = ""
            if len(s)==3:
                if s[0]!='0':
                    res += ones[s[0]] + " Hundred "+ numToString(s[1:])
                else:
                    res += numToString(s[1:])
            elif len(s)==2:
                if s[0]!='0':
                    if s[0]=='1':
                       res += special[s]
                    else: 
                        res += tens[s[0]] + " " + numToString(s[1])
                else:
                    res += numToString(s[1])
            elif s in ones:
                res += ones[s]
            return res
        if num==0:
            return 'Zero'
        res = ""
        d = {
            0:'',
            1: "Thousand",
            2: "Million",
            3: "Billion",
        }

        ones = {
            '1':"One",
            '2':'Two',
            '3':'Three',
            '4':'Four',
            '5':'Five',
            '6':'Six',
            '7':'Seven',
            '8':'Eight',
            '9':'Nine'
        }

        special = {
            "10":'Ten',
            '11':"Eleven",
            '12':'Twelve',
            '13':'Thirteen',
            '14':'Fourteen',
            '15':'Fifteen',
            '16':'Sixteen',
            '17':'Seventeen',
            '18':'Eighteen',
            '19':'Nineteen',
        }

        tens = {
            '2':'Twenty',
            '3':'Thirty',
            '4':'Forty',
            '5':'Fifty',
            '6':'Sixty',
            '7':'Seventy',
            '8':'Eighty',
            '9':'Ninety'
        }

        l = splitNum(str(num))
        ans = ""
        for i in range(len(l)-1,-1,-1):
            temp = numToString(l[i])
            ans += temp
            if i!=0 and temp:
                ans += " " + d[i] + " "
        res = []
        for i in ans.split():
            if i:
                if i[-1]==" ":
                    res.append(i[:-1])
                else:
                    res.append(i)
        return " ".join(res) 