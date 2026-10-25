class Solution:
    def encoder(self,s):
        encode=26*[0]
        for c in s:
                encode[ord(c)-ord('a')]+=1
        return tuple(encode)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Mymap={}
        for s in strs:
            encode=self.encoder(s)
            if encode in Mymap:
                Mymap[encode].append(s)
            else:
                Mymap[encode]=[s]
        return Mymap.values()
        