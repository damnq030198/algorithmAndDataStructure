
# # Python program to find maximum contiguous subarray 
   
# # Function to find the maximum contiguous subarray 
# from sys import maxsize
# def maxSubArraySum(a,size): 
       
#     max_so_far = -maxsize - 1
#     max_ending_here = 0
       
#     for i in range(0, size): 
#         max_ending_here = max_ending_here + a[i] 
#         if (max_so_far < max_ending_here): 
#             max_so_far = max_ending_here 
  
#         if max_ending_here < 0: 
#             max_ending_here = 0   
#     return max_so_far 
   
# # Driver function to check the above function  
# a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
# print("Maximum contiguous sum is", maxSubArraySum(a,len(a)) )


# Python program to print largest contiguous array sum 
  
from sys import maxsize 
  
# Function to find the maximum contiguous subarray 
# and print its starting and end index 
def maxSubArraySum(a,size): 
  
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(0,size): 
  
        max_ending_here += a[i] 
  
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
  
    print("Maximum contiguous sum is %d"%(max_so_far)) 
    print("Starting Index %d"%(start)) 
    print("Ending Index %d"%(end)) 

# a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
a = [-2, -3, 4, -1, -2, 1, 5, -3] 
maxSubArraySum(a,len(a)) 
