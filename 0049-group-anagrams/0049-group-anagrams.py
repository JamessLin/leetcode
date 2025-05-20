class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            c1 = [0]*26
            for i in word:
                n = ord(i) - ord('a')
                c1[n] += 1

            if tuple(c1) in map:
                map[tuple(c1)].append(word)
            else:
                map[tuple(c1)] = [word]

        return list(map.values())