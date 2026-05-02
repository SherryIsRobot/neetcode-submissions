class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}

        for x in nums:

            num_count[x] = num_count.get(x, 0) + 1

        sorted_items = sorted(num_count.items(), key=lambda x: x[1], reverse=True)

        result = []

        for key, freq in sorted_items[:k]:
            result.append(key)

        return result

sol=Solution()
print(sol.topKFrequent([1,2,2,3,3,3], 2))
