class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]
        return ''.join(strs)
            

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            n = int(s[i: j])
            res.append(s[j + 1: j + n + 1])
            i = j + n + 1
        return res


        
