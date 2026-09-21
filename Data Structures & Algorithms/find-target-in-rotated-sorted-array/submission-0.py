class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Found target
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:

                # Target lies inside sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                # Target lies inside sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1