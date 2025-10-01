test_set = "16,1,2,0,4,2,7,1,2,14".split(",")
test_set = [int(i) for i in test_set]

with open("ex7.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "")
        dataset = [int(i) for i in line.split(",")]

minimum = min(dataset)
maximum = max(dataset)

answer = float("inf")
for _ in range(minimum, maximum + 1):
    # result = sum(abs(i - _) for i in dataset) part 1
    result = sum(sum(range(abs(i - _) + 1)) for i in dataset)
    if answer > result:
        answer = result

print(answer)
