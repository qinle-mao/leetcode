# Double pointers
# i -> pointer_fast 
# curr_ptr -> pointer_slow
class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        count = 0
        prev = -10001
        curr_ptr = 0
        for i in range(len(nums)):
            if nums[i] != prev:
                k += count
                count = 1
                nums[curr_ptr] = nums[i]
                prev = nums[i]
                curr_ptr += 1
            elif count < 2:
                count += 1
                nums[curr_ptr] = nums[i]
                curr_ptr += 1
            else:
                continue
        if count <= 2:
            k += count
        return k
    
nums_1 = [1,1,1,2,2,3]
nums_2 = [0,0,1,1,1,1,2,3,3]
nums_3 = [1]
print(Solution().removeDuplicates(nums_3))
print(nums_3)
