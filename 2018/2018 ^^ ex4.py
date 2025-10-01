from datetime import datetime
from collections import Counter

with open("ex4.txt") as exercise:
    data = []

    for elt in exercise.readlines():
        elt = elt.strip()
        date = elt[1:17]
        minutes = elt[14:16]
        date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        info = elt[19:]
        elt = (date, info)
        data.append(elt)

data.sort(key=lambda x: x[0])

guards_times = {}
for line in data:
    if line[1].startswith("Guard"):
        guard = line[1].split(" ")[1]
        # print(guard)
    elif line[1].startswith("falls"):
        starting_minutes = int(line[0].strftime("%M"))
        # sleepytime = line[0] #precise asleep moment (part 2)
    elif line[1].startswith("wakes"):
        waking_minutes = int(line[0].strftime("%M"))
        minutes_asleep = [
            i + starting_minutes for i in range((waking_minutes - starting_minutes))
        ]
        # wakeup = line[0] #precise wakeup moment(part 2)
        # delta = wakeup - sleepytime
        # print(sleepytime, wakeup)
        # print(delta)
        if guard not in guards_times:
            guards_times[guard] = minutes_asleep
            # guards_times[guard] = delta
        else:
            guards_times[guard].extend(minutes_asleep)
            # guards_times[guard] += delta

print()

max_occurences = 0
worst_gard = None
guard_times = None
for guard, time in guards_times.items():
    occurences = Counter(time)
    worst_occ = occurences.most_common()[0][1]
    if max_occurences < worst_occ:
        max_occurences = worst_occ
        worst_min = occurences.most_common()
        worst_gard = int(guard[1:])

print(worst_gard * worst_min[0][0])

# print(guard, time)
