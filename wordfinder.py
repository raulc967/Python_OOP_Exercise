"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__():
        self.open = open("words.text", "r")
        self.words = self.open.read()
        print(f"{len(self.words)} words read")
    
    def random():
        ran_num = random.choice(self.words)
        count = 0
        for word in self.words:
            if count == ran_num:
                return word
            count = count + 1

class SpecialWordFinder(WordFinder):
    def parse(self, words):
        lst = []
        word.strip() for word in words:
            if word.strip() and not word.startswith("#"):
                lst.append(word)
        return lst