class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split(" ")
        if(len(s)!=len(pattern)):
            return False
        hash_map={}
        hash_map_s={}
        print(S)
        
        i=0
        for p in pattern:
            print(p,s[i],hash_map,hash_map_s, p in hash_map and s[i] in hash_map_s  )
            if(p in hash_map and hash_map[p]!=s[i] ):
                return False
            if s[i] in hash_map_s and hash_map_s[s[i]]!=p :
                return False
            else:
                hash_map[p]=s[i]
                hash_map_s[s[i]]=p
            i+=1
            
        
        print(hash_map_s,hash_map)
        return True
            
 



        