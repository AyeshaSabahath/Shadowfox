from collections import defaultdict
from spellchecker import SpellChecker

spell = SpellChecker()

class SmartKeyboard:
    def __init__(self, text_file):
        self.bigram_model = defaultdict(list)
        self.train_model(text_file)

    def train_model(self, text_file):
        with open(text_file, "r") as file:
            lines = file.readlines()

        for line in lines:
            words = line.lower().split()
            for i in range(len(words) - 1):
                self.bigram_model[words[i]].append(words[i + 1])

    def autocorrect_word(self, word):
        return spell.correction(word)

    def predict_next_word(self, word):
        word = word.lower()
        if word in self.bigram_model:
            predictions = self.bigram_model[word]
            return max(set(predictions), key=predictions.count)
        return "No suggestion"