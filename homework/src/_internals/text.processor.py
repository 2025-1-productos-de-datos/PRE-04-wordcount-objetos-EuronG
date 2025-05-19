class TextProcessor:

    def preprocess_lines(self, lines):
        return [line.lower().strip() for line in lines]
    
    def split_into_words(self, lines):
        words = []
        for line in lines:
            words.extend(word.strip(",.!?") for word in line.split())
        return words