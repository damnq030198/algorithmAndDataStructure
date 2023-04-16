class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        try:
            s = float(s)
            return True
        except:
            return False

# class Solution(object):
#     def isNumber(self, str):
#         """
#         :type s: str
#         :rtype: bool
#         """

#         i = 0
#         j = len(str) - 1
#         #remove
#         # Handling whitespaces 
#         while i<len(str) and str[i] == ' ': 
#             i += 1
#         while j >= 0 and str[j] == ' ': 
#             j -= 1

#         if i > j: 
#             return False

#         # if string is of length 1 and the only 
#         # character is not a digit 
#         if (i == j and not(str[i] >= '0' and str[i] <= '9')): 
#             return False

#         # If the 1st char is not '+', '-', '.' or digit 
#         if (str[i] != '.' and str[i] != '+' and 
#             str[i] != '-' and not(str[i] >= '0' and 
#             str[i] <= '9')): 
#             return False

#         # To check if a '.' or 'e' is found in given 
#         # string.We use this flag to make sure that 
#         # either of them appear only once. 
#         flagDotOrE = False
#         isNum = 0
#         t = i
#         for i in range(t,j + 1): 
#             # If any of the char does not belong to 
#             # {digit, +, -,., e} 
#             if (str[i] != 'e' and str[i] != '.' and 
#                 str[i] != '+' and str[i] != '-' and not
#                (str[i] >= '0' and str[i] <= '9')): 
#                 return False
#             if str[i] <= '0' and str[i] >= '9':
#                 isNum +=1
#             if str[i] == '.': 
                
#                 # check if the char e has already 
#                 # occured before '.' If yes, return 0 
#                 if flagDotOrE: 
#                     return False
#                 flagDotOrE = True
#                 if i == j:
#                     return True
#                 if i + 1 > len(str): 
#                     return False
#                 if (not(str[i + 1] >= '0' and 
#                         str[i + 1] <= '9')): 
#                     return False
#             elif str[i] == 'e': 

#                 # set flagDotOrE = 1 when e is encountered. 
#                 flagDotOrE = True
#                 if i ==j:
#                     return False

#                 # if there is no digit before e 
#                 if (not(str[i - 1] >= '0' and 
#                         str[i - 1] <= '9')): 
#                     return False

#                 # if e is the last character 
#                 if i + 1 > len(str): 
#                     return False

#                 # if e is not followed by 
#                 # '+', '-' or a digit 
#                 if (str[i + 1] != '+' and str[i + 1] != '-' and 
#                    (str[i + 1] >= '0' and str[i] <= '9')): 
#                     return False
#         if isNum == 0:
#             return False
#         # If the string skips all the 
#         # above cases, it must be a numeric string 
#         return True