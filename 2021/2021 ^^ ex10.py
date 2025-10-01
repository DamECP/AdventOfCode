import re


def reduce_line(line):
    valid = [r"{}", r"()", r"<>", r"[]"]

    changed = True
    while changed:
        changed = False

        for pattern in valid:
            found_pattern = re.search(re.escape(pattern), line)
            if found_pattern:
                line = line[: found_pattern.start()] + line[found_pattern.end() :]
                changed = True
                break

    return line


with open("ex10.txt") as exercise:

    score = 0
    valid_lines = []
    for line in exercise:
        line = line.replace("\n", "")

        closers = [">", "]", ")", "}"]

        reduced = reduce_line(line)

        first_closer = len(reduced)
        char = ""

        for closer in closers:
            if closer not in reduced:
                continue
            elif reduced.index(closer) < first_closer:
                first_closer = reduced.index(closer)
                char = closer

        if char == ")":
            score += 3
        elif char == "]":
            score += 57
        elif char == "}":
            score += 1197
        elif char == ">":
            score += 25137

        else:
            valid_lines.append(line)


all_scores = []
for line in valid_lines[:-1]:
    line_score = 0
    line = reduce_line(line)[::-1]

    print(line)

    for char in line:
        line_score *= 5
        if char == "(":
            line_score += 1
        elif char == "[":
            line_score += 2
        elif char == "{":
            line_score += 3
        elif char == "<":
            line_score += 4

    all_scores.append(line_score)

print(sorted(all_scores)[len(all_scores) // 2])
