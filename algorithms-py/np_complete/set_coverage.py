
from ds.priority_dictionary import MaxPriorityDictionary
import unittest


class SetCoverage:
    """
    Find solution for set coverage problem.
    This problem is NP complete, so we will use greedy approach.
    """
    def __init__(self, sets):

        self.sets = sets
        self.union = set()
        self.element_to_set = {}

        for single_set in sets:
            for value in single_set:

                self.union.add(value)

                if value in self.element_to_set:
                    self.element_to_set[value].append(single_set)
                else:
                    self.element_to_set[value] = [single_set]

    def find_coverage(self):

        data = []

        for single_set in self.sets:
            data.append((single_set, len(single_set)))

        max_heap = MaxPriorityDictionary(data)

        left_to_cover = len(self.union)

        coverage = []

        while left_to_cover != 0:

            cur_set = max_heap.extract_max()

            for elem in cur_set:

                 # decrease priority for other sets according to covered elements
                if elem in self.element_to_set:
                    for set_to_decrease in self.element_to_set[elem]:
                        if set_to_decrease is not cur_set:
                            max_heap.decrease_priority(set_to_decrease, 1)

                    left_to_cover -= 1
                    self.element_to_set.pop(elem, None)

            coverage.append(cur_set)

        return coverage


class SetCoverageTest(unittest.TestCase):

    def test_coverage(self):
        set_coverage = SetCoverage([frozenset(["a", "d"]), frozenset(["c"]), frozenset(["b", "d", "e"]),
                                    frozenset(["a", "c", "d"])])
        coverage = set_coverage.find_coverage()

        self.assertEquals(2, len(coverage))

        self.assertEquals([frozenset(["a", "c", "d"]), frozenset(["b", "d", "e"])], coverage)


if __name__ == "__main__":
    unittest.main()