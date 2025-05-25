class PreprocessLinesMixin:
    def preprocess_lines(self):
        self.preprocessed_lines = [line.lower().strip() for line in self.lines]