class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if(len(strs)==1):
            return[strs]
        hash_map={}
        # print("".join(sorted(strs[0])), strs)
        for s in strs:
            _s="".join(sorted(s))
            print(_s,s,_s not in hash_map)
            if(_s not in hash_map):

                hash_map[_s] = []
                hash_map[_s].append(s)
            else:
                strs
                hash_map[_s].append(s)

        print(hash_map)
        return list(hash_map.values())

        