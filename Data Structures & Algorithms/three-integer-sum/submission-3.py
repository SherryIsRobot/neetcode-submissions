class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since nums is sorted, no solution is possible after this
            if nums[i] > 0:
                break

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicates
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return result