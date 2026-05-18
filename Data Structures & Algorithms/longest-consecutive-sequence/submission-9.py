class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sort_num = sorted(nums)

        count = 1
        max_count = 1

        for i in range(len(sort_num) - 1):
            if sort_num[i + 1] == sort_num[i]:
                continue

            elif sort_num[i + 1] == sort_num[i] + 1:
                count += 1
                max_count = max(max_count, count)

            else:
                count = 1

        return max_count