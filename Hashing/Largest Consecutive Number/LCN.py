class Solution:
    def longestConsecutive(self, nums):
        if len(nums)==0:
            return 0;
        st = set(nums)
        longest = 1
        for e in st:
            if e-1 not in st:
                count = 1
                x = e
            while x+1 in st:
                x = x+1
                count = count+1
            longest = max(count, longest)
        return longest



if __name__ == "__main__":
    a = [100, 4, 200, 1, 3, 2] 
    solution = Solution()
    ans = solution.longestConsecutive(a)
    print("Solution: ", ans)