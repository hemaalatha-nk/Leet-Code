class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if(len(strs)==1):
            return[strs]
        hash_map={}
        for s in strs:
            _s="".join(sorted(s))
            if(_s not in hash_map):
                hash_map[_s] = []
            hash_map[_s].append(s)

        return list(hash_map.values())

        