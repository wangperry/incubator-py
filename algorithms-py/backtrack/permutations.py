

class PermutationsGenerator():

    def __init__(self, base_arr):
        self.base_arr = base_arr
        self.permutations = []
        self.__generate_rec([])

    def get_permutations(self):
        return self.permutations

    def __generate_rec(self, cur):

        if len(cur) == len(self.base_arr):
            self.permutations.append([value for value in cur])
            return

        for value in self.base_arr:
            if not value in cur:
                cur.append(value)
                self.__generate_rec(cur)
                cur.remove(value)

def main():
    perm = PermutationsGenerator(["A", "B", "C"])
    for single_perm in perm.get_permutations():
        print(str(single_perm))

if __name__ == "__main__":
    main()




