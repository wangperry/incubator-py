__author__ = 'admin'

import math

class Trigram:

    length = 0

    def __init__(self, file_path):
        self.data = {}
        self.parse_file(file_path)

    def parse_file(self, fn):
        pair = '  '

        with open(fn) as file_descriptor:
            for line in file_descriptor:
                for letter in line.strip():
                    d = self.data.setdefault(pair, {})
                    d[letter] = d.get(letter, 0) + 1
                    pair = pair[1] + letter

        self.measure()


    def measure(self):
        """calculates the scalar length of the trigram vector and stores it in self.length."""
        total = 0
        for y in self.data.values():
            total += sum([x * x for x in y.values()])
        self.length = math.sqrt(total)

    def similarity(self, other):
        """returns a number between 0 and 1 indicating similarity.
        1 means an identical ratio of trigrams;
        0 means no trigrams in common.
        """
        if not isinstance(other, Trigram):
            raise TypeError("can't compare Trigram with non-Trigram")
        data1 = self.data
        data2 = other.data
        total = 0
        for k in data1.keys():
            if k in data2:
                a = data1[k]
                b = data2[k]
                for x in a:
                    if x in b:
                        total += a[x] * b[x]

        return float(total) / (self.length * other.length)


def detect_language(unknown, languages):
    max_similarity = 0.0
    detected_language = None

    for language, trigram in languages.items():
        cur_similarity = unknown.similarity(trigram)
        if cur_similarity > max_similarity:
            max_similarity = cur_similarity
            detected_language = language

    return detected_language

def main():

    languages = {
        "english": Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/english.txt"),
        "dutch": Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/dutch.txt"),
        "finnish": Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/finnish.txt"),
        "italian": Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/italian.txt"),
        "spanish": Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/spanish.txt"),
        "swedish": Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/swedish.txt")}

    unknown1 = Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/unknown_spanish.txt")
    unknown2 = Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/unknown_english.txt")

    print "Detected language: %s" % detect_language(unknown1, languages)
    print "Detected language: %s" % detect_language(unknown2, languages)


if __name__ == "__main__":
    main()
