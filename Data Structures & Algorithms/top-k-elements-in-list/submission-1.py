
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        # Count the frequency of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Create buckets indexed by frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # Collect the k most frequent numbers
        result = []

        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result