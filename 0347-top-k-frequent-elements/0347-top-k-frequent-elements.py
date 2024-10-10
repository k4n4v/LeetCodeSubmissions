class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        top_k_vals = [key for key,_ in sorted(count.items(), key=lambda item: item[1], reverse=True)[:k]]
        
        return top_k_vals
    
        # Time: O(nlogn)
        # Space: O(n)
            