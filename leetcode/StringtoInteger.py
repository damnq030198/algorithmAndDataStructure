class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        string = str
        if not string:
            return 0
        string = string.strip()
        if string == "":
            return 0
        number, flag = 0,1
        if string[0]=='-':
            string = string[1:]
            flag = -1
        elif string[0] == "+":
            string = string[1:]
        for c in string:
            if c>='0' and c<='9':
                number = 10*number + ord(c) - ord('0') 
            else:
                break
        number = flag * number
        number = number if number <= 2**31-1 else 2**31-1
        number = number if number >= -2**31 else -2**31
        return number