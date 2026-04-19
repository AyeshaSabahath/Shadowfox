from collections import defaultdict, Counter
from spellchecker import SpellChecker

spell = SpellChecker()

class SmartKeyboard:
    def __init__(self, text_file):
        self.spell = SpellChecker()
        self.bigram_model = defaultdict(list)
        self.word_frequency = Counter()
        self.train_model(text_file)

    def train_model(self, text_file):
        with open(text_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            words = line.lower().strip().split()

            for word in words:
                self.word_frequency[word] += 1

            for i in range(len(words) - 1):
                current_word = words[i]
                next_word = words[i + 1]
                self.bigram_model[current_word].append(next_word)

    def autocorrect_sentence(self, sentence):
        words = sentence.split()
        corrected_words = []

        for word in words:
            clean_word = word.strip(".,!?")

            # Get correction
            corrected = self.spell.correction(clean_word)

            # If no correction found, keep original
            if corrected is None:
                corrected = clean_word

            # Preserve capitalization (for "I")
            if word.istitle():
                corrected = corrected.capitalize()

            corrected_words.append(corrected)

        return corrected_words

    def predict_next_words(self, last_word, top_n=3):
        last_word = last_word.lower()

        if last_word not in self.bigram_model:
            return ["No suggestion"]

        predictions = self.bigram_model[last_word]

        ranked_predictions = Counter(predictions).most_common(top_n)

        return [word for word, _ in ranked_predictions]