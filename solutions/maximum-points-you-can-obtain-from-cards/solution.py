class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_sum=sum(cardPoints)
        n=len(cardPoints)
        if n==k:
            return total_sum

        window_size=n-k
        c_w_s=sum(cardPoints[:window_size])
        min_w_s=c_w_s
        for i in range(window_size,n):
            c_w_s+=cardPoints[i]-cardPoints[i-window_size]
            min_w_s=min(min_w_s,c_w_s)
        return total_sum-min_w_s

        