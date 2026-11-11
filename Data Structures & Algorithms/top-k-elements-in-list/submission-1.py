class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for val in nums:
            seen[val] = 1 + seen.get(val, 0)

        freq = [[] for i in range(len(nums) + 1)]

        for val, cnt in seen.items():
            freq[cnt].append(val)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for new in freq[i]:
                res.append(new)
                if len(res) == k:
                    return res


        