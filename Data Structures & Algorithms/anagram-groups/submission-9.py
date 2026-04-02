class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for s in strs:
            counter = [0] * 28
            for c in s:
                #En que posición está
                counter[ord(c) - ord('a')] += 1
            hashMap[tuple(counter)].append(s)
        
        return list(hashMap.values())