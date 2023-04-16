class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s)%2 == 1:
            return False
        dic= {"(": ")","{": "}","[": "]"}
        stack = []
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                close = stack.pop()
                if c != dic[close]:
                    return False
        return len(stack) == 0