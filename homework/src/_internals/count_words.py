class CountWordsMinxinMixin:
    def count_words(self):

        word_counts = {}

        for word in self.words:
            word_counts[word] = word_counts.get(word, 0) + 1

        self.word_counts = word_counts