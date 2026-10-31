class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i< len(word) and j< len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha() or abbr[j] == "0":
                return False
            else:
                sublen = []
                while j< len(abbr) and not abbr[j].isalpha():
                    sublen.append(abbr[j])
                    j += 1
                i += int(''.join(sublen))
        return i == len(word) and j == len(abbr)

        