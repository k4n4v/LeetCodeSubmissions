class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        
        for sentence in sentences:
            split_sentence = sentence.split(" ")
            max_words = max(max_words, len(split_sentence))
        
        return max_words