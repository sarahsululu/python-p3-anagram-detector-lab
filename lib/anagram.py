# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        matches = []
        for candidate in candidates:
            if candidate.lower() != self.word:
                if sorted(candidate.lower()) == sorted(self.word):
                    matches.append(candidate)
        return matches

