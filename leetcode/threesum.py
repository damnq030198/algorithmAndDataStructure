class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ls =[]
        i =0
        while i<len(nums)-2:
            if nums[i] >0:
                return ls
            l=i+1
            r=len(nums) -1
            while l<r:
                if nums[l] +nums[r] < -nums[i]:
                    while l+1 <r+1 and nums[l] ==nums[l+1]:
                        l+=1
                    l+=1
                elif nums[l]+ nums[r]> -nums[i]:
                    while r-1>l-1 and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                else:
                    ls.append([nums[i], nums[l],nums[r]])
                    while l+1 <r+1 and nums[l] ==nums[l+1]:
                        l+=1
                    l+=1
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return ls
def main():
    nums =[-4,-8,7,13,10,1,-14,-13,0,8,6,-13,-5,-4,-12,2,-11,7,-5,0,-9,-14,-8,-9,2,-7,-13,-3,13,9,-14,-6,8,1,14,-5,-13,8,-10,-5,1,11,-11,3,14,-8,-10,-12,6,-8,-5,13,-15,2,11,-5,10,6,-1,1,0,0,2,-7,8,-6,3,3,-13,8,5,-5,-3,9,5,-4,-14,11,-8,7,10,-6,-3,11,12,-14,-9,-1,7,5,-15,14,12,-5,-8,-2,4,2,-14,-2,-12,6,8,0,0,-2,3,-7,-14,2,7,12,12,12,0,9,13,-2,-15,-3,10,-14,-4,7,-12,3,-10]#[-1,0,1,2,-1,-4]# [0,0,0,0]#
    s = Solution()
    ls = s.threeSum(nums)
    print (ls)

main()