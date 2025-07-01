class Solution:
    def possibleStringCount(self, word: str) -> int:
        possibleVal = 1
        w = ""
        for i in word: 
            if w != i:
                w = i
            else:
                possibleVal +=1

        return possibleVal