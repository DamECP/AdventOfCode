def f(numbers):
    max_ = len(numbers) // 2
    return numbers[:max_]


my_seat = 868
seats = []
with open("ex5.txt") as exercise:
    max_n = 0
    for line in exercise:
        numbers = [i for i in range(128)]
        columns = [i for i in range(8)]

        line = line.replace("\n", "")

        for i in line[:7]:
            # print(i)
            half = len(numbers) // 2
            if i == "F":
                numbers = numbers[:half]
                # print(numbers)
            if i == "B":
                numbers = numbers[half:]
                # print(numbers)
            row = numbers[0]
        for i in line[7:]:
            # print(i)
            half = len(columns) // 2
            if i == "R":
                columns = columns[half:]
                # print(columns)
            if i == "L":
                columns = columns[:half]
                # print(columns)
            column = columns[0]
            # print(column)
        seat = row * 8 + column
        seats.append(seat)
        if seat > max_n:
            max_n = seat

seats = sorted(seats)

for i, seat in enumerate(seats):
    if not seats[i - 1] and not seats[i + 1]:
        print(seat)
