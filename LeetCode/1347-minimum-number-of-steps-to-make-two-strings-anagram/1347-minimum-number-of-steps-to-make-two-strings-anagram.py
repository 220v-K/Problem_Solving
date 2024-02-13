class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ds = {}
        dt = {}

        for c in s:
            ds[c] = ds.get(c, 0) + 1
        for c in t:
            dt[c] = dt.get(c, 0) + 1
            
        result = 0

        for c in ds.keys():
            temp = ds[c] - dt.get(c, 0)
            if temp > 0:
                result += temp
            
        return result