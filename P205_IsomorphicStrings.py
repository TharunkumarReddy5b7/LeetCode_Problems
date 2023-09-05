#Given two strings s and t, determine if they are isomorphic.

#Two strings s and t are isomorphic if the characters in s can be replaced to get t.

#All occurrences of a character must be replaced with another character while preserving
#the order of characters. No two characters may map to the same character, but a character
#may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m={}

        for i in range(len(s)):
            if s[i] not in m:
                if t[i] in m.values():
                    return False
                else:
                    m[s[i]]=t[i]
            else:
                r=m[s[i]]
                if r==t[i]:
                    continue
                else:
                    return False
        else:
            return True
