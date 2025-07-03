class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        sort = sorted(seen.items(), key=lambda item: item[1], reverse=True)
        
        res = []
        for i in range(k):
            res.append(sort[i][0])
        return res

        # return[item[0] for item in sort[:k]]