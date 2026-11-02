class Solution:
   
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0

        longest_sub = set()
        c = 0
        i = 0
        left = 0
        max_count = 0

        while i < n:
            if s[i] not in longest_sub:
                longest_sub.add(s[i])
                c += 1
                i += 1
                max_count = max(max_count, c)

            else:
                longest_sub.remove(s[left])
                left += 1
                c -= 1

        return max_count




