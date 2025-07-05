class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only start counting if num is the beginning of a sequence
            if (num - 1) not in num_set:
                current = num
                streak = 1

                # Count the length of the sequence
                while (current + 1) in num_set:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest
