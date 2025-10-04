import operator


def part_1(inputs: list[int], target):
    operations = [operator.add, operator.mul]

    def all_solutions(inputs: list[int], operations=operations):
        if len(inputs) == 1:
            return [inputs[0]]
        results = []
        for op in operations:
            answer = op(inputs[0], inputs[1])
            new_list = [answer] + inputs[2:]
            results.extend(all_solutions(new_list, operations))
        return results

    return target in all_solutions(inputs, operations)


def part_2(inputs: list[int], target):

    def concatenation(a: int, b: int) -> int:
        return int(str(a) + str(b))

    operations = [operator.add, operator.mul, concatenation]

    def depth_first_search(inputs: list[int]) -> bool:
        if len(inputs) == 1:
            return inputs[0] == target

        for op in operations:
            answer = op(inputs[0], inputs[1])
            new_list = [answer] + inputs[2:]
            if depth_first_search(new_list):
                return True
        return False

    return depth_first_search(inputs)


answer_1 = 0
answer_2 = 0
with open("ex7.txt") as exercise:

    for line in exercise:
        line = line.replace("\n", "")
        expected, numbers = line.split(":")
        expected = int(expected)
        numbers = [int(i) for i in numbers.split()]

        if part_1(numbers, expected):
            answer_1 += expected

        if part_2(numbers, expected):
            answer_2 += expected

print(answer_1)
print(answer_2)
