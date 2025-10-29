class Dir:
    def __init__(self, name):
        self.name = name
        self.content = []
        self.size = 0

    def add_content(self, content):
        self.content.extend([content])

    def get_size(self):
        sub_total = sum([i.size for i in self.content])
        self.size += sub_total

    def __repr__(self):
        return f"{self.name} {self.size}"


with open("ex7.txt") as exercise:
    data = [line.strip() for line in exercise]


directories = {}


for index, line in enumerate(data):
    if "cd" in line and "ls" in data[index + 1]:
        name = line.split(" ")[-1]

        if name not in directories:
            d = Dir(name)
            directories[name] = d
        else:
            d = directories[name]

        for ls_lines in data[index + 2 :]:

            if "$" in ls_lines:
                break

            if ls_lines.startswith("dir"):
                inner_name = ls_lines.split(" ")[-1]

                if inner_name not in directories:
                    inner_dir = Dir(inner_name)
                    directories[inner_name] = inner_dir

                else:
                    inner_dir = directories[inner_name]

                d.add_content(inner_dir)

            else:
                file_value = int(ls_lines.split(" ")[0])
                d.size += file_value

        directories[name] = d


def dfs(d: Dir, visited=None):
    if visited is None:
        visited = set()
    if id(d) in visited:
        return 0  # déjà compté
    visited.add(id(d))
    total = d.size
    for c in d.content:
        if isinstance(c, Dir):
            total += dfs(c, visited)
    d.size = total
    return total


root = directories["/"]
dfs(root)

unused = 70000000 - root.size
delta = 30000000 - unused

answer_2 = min([i.size for i in directories.values() if i.size > delta])
print(answer_2)
