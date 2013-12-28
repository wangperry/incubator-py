

class KGram:

    def __init__(self, name, k=5, file_path=None):
        self.name = name
        self.k = k
        self.data = {}
        self.length = 0
        if file_path is not None:
            self.add_data(file_path)

    def add_data(self, file_path):
        with open(file_path) as file_descriptor:
            for line in file_descriptor:
                cleared_line = self.clear_line(line)
                self.store_line(cleared_line)

    def store_line(self, line):

        if len(line) <= self.k:
            if not line in self.data:
                self.data[line] = 1
            else:
                self.data[line] += 1

        else:

            off = self.k

            for i in range(off-1, len(line)):
                gram = line[i-off+1:i+1]

                self.length += 1

                if not gram in self.data:
                    self.data[gram] = 1
                else:
                    self.data[gram] += 1

    def similarity(self, other):
        """
        Calculate Jaccard similarity coefficient.
        """
        intersection_count = 0
        union_count = self.length + other.length

        for key, value in self.data.items():
            if key in other.data:
                intersection_count += min(value, other.data[key])

        return float(intersection_count)/union_count



    @staticmethod
    def clear_line(line):
        cleared_line = line.strip().lower()
        cleared_line = cleared_line.replace(".", "")
        cleared_line = cleared_line.replace(":", "")
        cleared_line = cleared_line.replace(";", "")
        cleared_line = cleared_line.replace("!", "")
        cleared_line = cleared_line.replace("?", "")
        cleared_line = cleared_line.replace(",", "")
        return " ".join(cleared_line.split())

def main():

    k = 5

    arr = [
        KGram("english", k, "/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/english.txt"),
        KGram("spanish", k, "/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/spanish.txt"),
        KGram("dutch", k, "/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/dutch.txt"),
        KGram("swedish", k, "/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/swedish.txt"),
        KGram("italian", k, "/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/italian.txt"),
        KGram("finnish", k, "/Users/admin/repo/incubator-py/algorithms-py/nlp/languages/finnish.txt")
    ]

    simple = KGram("simple", k, "/Users/admin/repo/incubator-py/algorithms-py/nlp/simple.txt")

    most_sim = None
    max_sim = -1.0

    for cur in arr:

        sim_value = simple.similarity(cur)

        if sim_value > max_sim:
            max_sim = sim_value
            most_sim = cur

    print "Most similar '%s': %s" % (most_sim.name, max_sim)




if __name__ == "__main__":
    main()

