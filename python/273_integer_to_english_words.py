class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        rst = ""
        tmp = num % 1000
        rst = rst + self.castNum(tmp)
        num = num / 1000
        t = 1
        while num > 0:
            t = t + 1
            tmp = num % 1000
            trst = self.castNum(tmp)
            tmprst = ""
            if trst != "":
                tmprst = trst + " " + self.Units(t)
            else:
                tmprst = ""
            print tmprst
            if tmprst != "":
                if rst != "":
                    rst = tmprst + " " + rst
                else:
                    rst = tmprst
            num = num/1000
        return rst

    def castNum(self, num):
        if num == 0:
            return ""
        hundred = num/100
        ten = num%100
        hun = self.castHundred(hundred)
        t = self.castTens(ten)
        if hun != "" and t != "":
            return hun + " " + t
        if  hun != "" and t == "":
            return hun
        if hun == "" and t != "":
            return t

    def castHundred(self, num):
        rst = ""
        if num != 0:
            rst = rst + self.Digit(num) + " " + self.Units(1)
        return rst

    def castTens(self, num):
        if num == 0:
            return ""
        ten = num / 10
        digit = num % 10
        rst = ""
        if ten != 0:
            if digit == 0:
                rst = rst + self.Tens(ten)
            else:
                if ten == 1:
                    rst = rst + self.TenToNineteen(num)
                else:
                    rst = rst + self.Tens(ten)
                    rst = rst + " "
                    rst = rst + self.Digit(digit)
        else:
            if digit == 0:
                return rst
            else:
                rst = rst + self.Digit(digit)
        return rst


    def Units(self, num):
        if num == 1:
            return "Hundred"
        elif num == 2:
            return "Thousand"
        elif num == 3:
            return "Million"
        elif num == 4:
            return "Billion"
    
    def Tens(self, num):
        if num == 1:
            return "Ten"
        elif num == 2:
            return "Twenty"
        elif num == 3:
            return "Thirty"
        elif num == 4:
            return "Forty"
        elif num == 5:
            return "Fifty"
        elif num == 6:
            return "Sixty"
        elif num == 7:
            return "Seventy"
        elif num == 8:
            return "Eighty"
        else:
            return "Ninety"

    def TenToNineteen(self, num):
        if num == 10:
            return "Ten"
        elif num == 11:
            return "Eleven"
        elif num == 12:
            return "Twelve"
        elif num == 13:
            return "Thirteen"
        elif num == 14:
            return "Fourteen"
        elif num == 15:
            return "Fifteen"
        elif num == 16:
            return "Sixteen"
        elif num == 17:
            return "Seventeen"
        elif num == 18:
            return "Eighteen"
        else:
            return "Nineteen"

    def Digit(self, num):
        if num == 0:
            return "Zero"
        elif num == 1:
            return "One"
        elif num == 2:
            return "Two"
        elif num == 3:
            return "Three"
        elif num == 4:
            return "Four"
        elif num == 5:
            return "Five"
        elif num == 6:
            return "Six"
        elif num == 7:
            return "Seven"
        elif num == 8:
            return "Eight"
        else:
            return "Nine"

x = Solution()
print x.numberToWords(1000010)