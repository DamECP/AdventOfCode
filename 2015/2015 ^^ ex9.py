graphes = {}

with open("ex9.txt") as exercise:
    for line in exercise:
        line = line.replace("\n", "").split(" ")
        city_1, city_2, distance = line[0], line[2], int(line[-1])

        if city_1 not in graphes:
            graphes[city_1] = {}
        graphes[city_1][city_2] = distance

        if city_2 not in graphes:
            graphes[city_2] = {}
        graphes[city_2][city_1] = distance


def all_paths(graph):
    solutions = []

    def dfs(current, arrival, path, total_distance, visited):
        if current == arrival:
            solutions.append((path.copy(), total_distance))
            return
        else:
            for destination, km in graph[current].items():
                if destination not in visited:
                    visited.add(destination)
                    path.append(destination)
                    dfs(destination, arrival, path, total_distance + km, visited)
                    path.pop()
                    visited.remove(destination)

    cities = list(graphes.keys())

    for i, start in enumerate(cities):
        for arrival in cities[i:]:
            dfs(start, arrival, [start], 0, set([start]))

    return solutions


test = all_paths(graphes)
test = [i for i in test if len(i[0]) == 8 and i[-1] != 0]

smallest_path = min([i[-1] for i in test])
longuest_path = max([i[-1] for i in test])
print(smallest_path)
print(longuest_path)
