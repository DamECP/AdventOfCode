with open("ex9.txt") as exercise:
    data = exercise.read().strip()


def clean_up(string):
    i = 0
    output = ""
    inside_brackets = False
    counter_cancelled = 0
    while i < len(string):
        if string[i] == "!":
            i += 2
        elif inside_brackets:
            if string[i] == ">":
                inside_brackets = False
            else:
                counter_cancelled += 1
            i += 1
        elif string[i] == "<":
            inside_brackets = True
            i += 1
        else:
            output += string[i]
            i += 1
    return output, counter_cancelled


cleaned_string = clean_up(data)[0].replace(",", "")
print(clean_up(data)[1])

total_value = 0
current_value = 0
for char in cleaned_string:
    if char == "{":
        current_value += 1
    elif char == "}":
        total_value += current_value
        current_value -= 1

print(total_value)
