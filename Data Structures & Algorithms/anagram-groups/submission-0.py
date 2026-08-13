class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for word in strs:
            x=sorted(word)
            key="".join(x)
            if key not in groups:
                groups[key]=[]
            groups[key].append(word)
        return list(groups.values())
