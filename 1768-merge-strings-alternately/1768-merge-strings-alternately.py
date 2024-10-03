class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        length = min(len(word1),len(word2)) # find the shortest length for the loop

        s = [] # array to store letters
        for i in range(length):
            # append word1 char first then word2 char
            s.append(word1[i])
            s.append(word2[i])
        
        # based on which one is longer it will execute the next lines
        # splice the word starting from the length index and append the remaining letters 
        s.append(word1[length:]) 
        s.append(word2[length:])

        # join array into a string and return
        return ''.join(s)
            