class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # num1 + num2 + num 3 = 0
        # num2 + num3 = -num1

        nums.sort()
        answer = list()
        for idx in range(len(nums)):

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left, right = idx + 1, len(nums) - 1
            while left < right:

                target = nums[idx] + nums[left] + nums[right]
                
                if target == 0:
                    answer.append(
                        [
                            nums[idx],
                            nums[left],
                            nums[right]
                        ]
                    )

                    left +=1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif target < 0:
                    left += 1
                else:
                    right -= 1       
        
        return answer

                
            