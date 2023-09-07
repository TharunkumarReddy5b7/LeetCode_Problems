#2828. Check if a String Is an Acronym of Words
'''Input: words = ["alice","bob","charlie"], s = "abc"
Output: true
Explanation: The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and 'c', respectively. Hence, s = "abc" is the acronym.'''


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        d=""
        for i in words:
            d+=i[0]
        if d==s:
            return True
        else:
            return False
