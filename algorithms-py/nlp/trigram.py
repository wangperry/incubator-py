__author__ = 'admin'

import math


class Trigram:

    """
    Class that represents trigrams.
    """

    def __init__(self, file_path):
        self.__vector = Trigram.__create_trigrams(file_path)
        self.__trigram_length = Trigram.__calculate_scalar_length(self.__vector)

    @staticmethod
    def __create_trigrams(file_path):
        """ Create dictionary of all trigrams from specified file path. """
        trigram_dic = {}

        with open(file_path) as file_descriptor:

            for line in file_descriptor:
                cleared_line = line.strip()

                for i in range(0, len(cleared_line)-2):

                    gram = line[i:i+3]

                    if not gram in trigram_dic:
                        trigram_dic[gram] = 1
                    else:
                        trigram_dic[gram] += 1

        return trigram_dic

    @staticmethod
    def __calculate_scalar_length(vector):
        """Calculates the scalar length of the trigram vector."""
        total = 0
        for freq in vector.values():
            total += freq * freq
        return math.sqrt(total)

    def similarity(self, other):
        """Returns a number between 0 and 1 indicating similarity.
        1 - means an identical ratio of trigrams;
        0 - means no trigrams in common.
        """
        if not isinstance(other, Trigram):
            raise TypeError("can't compare Trigram with non-Trigram")

        data1 = self.__vector
        data2 = other.__vector

        total = 0.0
        for key in data1.keys():
            if key in data2:
                total += data1[key] * data2[key]

        return total / (self.__trigram_length * other.__trigram_length)


class LanguageDetector:

    def __init__(self):
        self.languages = {
            "english": Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/english.txt"),
            "dutch": Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/dutch.txt"),
            "finnish": Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/finnish.txt"),
            "italian": Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/italian.txt"),
            "spanish": Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/spanish.txt"),
            "swedish": Trigram("/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/swedish.txt")}

    def detect_language(self, file_path):

        trigram_to_detect = Trigram(file_path)

        max_similarity = 0.0
        detected_language = None

        for language, trigram in self.languages.items():
            cur_similarity = trigram_to_detect.similarity(trigram)
            if cur_similarity > max_similarity:
                max_similarity = cur_similarity
                detected_language = language

        return detected_language


def main():

    lang_detector = LanguageDetector()

    file1 = "/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/unknown_spanish.txt"
    file2 = "/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/unknown_english.txt"

    print "Detected language: %s" % lang_detector.detect_language(file1)
    print "Detected language: %s" % lang_detector.detect_language(file2)


if __name__ == "__main__":
    main()
