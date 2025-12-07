from functools import lru_cache

with open("ex7.txt") as exercise:
    data = [i.strip() for i in exercise.readlines()]


def part_1():

    def splitters_positions(line: str) -> list[int]:
        return [i for i, char in enumerate(line) if char == "^"]

    def separate(cursors: set, splitter: list[int]) -> set:
        new_cursors = set()
        for c in cursors:
            if c in splitter:
                new_cursors.update((c - 1, c + 1))
            else:
                new_cursors.add(c)
        return new_cursors

    def splits(cursors: set, splitter: list[int]) -> int:
        return len([True for c in cursors if c in splitter])

    cursors = set([data[0].find("S")])
    answer_1 = 0

    for line in data:
        pos = splitters_positions(line)
        answer_1 += splits(cursors, pos)
        cursors = separate(cursors, pos)

    print(answer_1)


def part_2():

    start = (0, data[0].find("S"))
    max_y = len(data)
    max_x = len(data[0])

    splitters = {
        y: {x for x, c in enumerate(line) if c == "^"} for y, line in enumerate(data)
    }

    @lru_cache
    def dfs(y, x):
        if x < 0 or x >= max_x:
            return 0

        if y == max_y - 1:
            return 1

        new_y = y + 1

        if x in splitters[new_y]:
            return dfs(new_y, x - 1) + dfs(new_y, x + 1)

        return dfs(new_y, x)

    print(dfs(*start))


if __name__ == "__main__":
    part_1()
    part_2()
