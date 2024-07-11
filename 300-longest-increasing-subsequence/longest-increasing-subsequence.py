class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [1] * n
        hash_map = list(range(n))

        for i in range(n):
            for prev_index in range(i):
                if arr[prev_index] < arr[i] and 1 + dp[prev_index] > dp[i]:
                    dp[i] = 1 + dp[prev_index]
                    hash_map[i] = prev_index

        ans = -1
        last_index = -1

        for i in range(n):
            if dp[i] > ans:
                ans = dp[i]
                last_index = i
        return ans
        

        temp = [arr[last_index]]

        while hash_map[last_index] != last_index:
            last_index = hash_map[last_index]
            temp.append(arr[last_index])

        temp.reverse()