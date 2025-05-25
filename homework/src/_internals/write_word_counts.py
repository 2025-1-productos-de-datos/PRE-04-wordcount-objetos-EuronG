import os


class WriteWordCountsMixin:
    def write_word_counts(self):

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        output_file = os.path.join(self.output_folder, "wordcount.tsv")

        with open(output_file, "w", encoding="utf-8") as f:
            for word, count in self.word_counts.items():
                f.write(f"{word}\t{count}\n")