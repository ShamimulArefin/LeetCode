# one way

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1),len(word2))):
            res += word1[i]+word2[i]
        return res+word1[i+1:]+word2[i+1:]
    
# another way

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        res = ""
        if len(word1)<len(word2):
            for i in range(len(word1)):
                s += word1[i]+word2[i]
            res = s+word2[len(word1):]
        elif len(word1)>len(word2):
            for i in range(len(word2)):
                s += word1[i]+word2[i]
            res = s+word1[len(word2):]
        else:
            for i in range(len(word1)):
                s += word1[i]+word2[i]
            res = s
        return res