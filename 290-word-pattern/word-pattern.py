class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(" ")
        if(len(s)!=len(pattern)):
            return False
        hash_map={}
        hash_map_s={}
        # print(S)
        
        for c,w in zip(pattern,s):
            # print(c,w,hash_map,hash_map_s, p in hash_map and s[i] in hash_map_s  )
            if(c in hash_map and hash_map[c]!=w):
                return False
            if w in hash_map_s and hash_map_s[w]!=c:
                return False
            else:
                hash_map[c]=w
                hash_map_s[w]=c
            
        
        # print(hash_map_s,hash_map)
        return True
            
 



        