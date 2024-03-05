class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        return citations[n//2]