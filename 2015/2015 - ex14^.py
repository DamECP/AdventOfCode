class Reindeer():

    def __init__(self, name:int, speed: int, time: int, rest: int):
        self.name = name
        self.speed = speed
        self.time = time
        self.rest = rest

    def __str__(self):
        return f"{self.name} ; {self.speed} ; {self.time} ; {self.rest} "

    def trajet(self, seconds:int):
        total_time = 0
        km = 0
        while total_time <= seconds:
            if total_time + self.time + self.rest <= seconds:
                km += self.speed * self.time
                total_time += self.time + self.rest
            else:
                remaining_time = seconds - total_time
                if remaining_time >= self.time:
                    km+= self.speed * self.time
                    total_time += remaining_time
                else :
                    km += self.speed * remaining_time
                    total_time += remaining_time
                    break
        
        return f"{self.name} => {total_time} sec : {km}km"


reindeers = []

with open('ex14.txt') as exercise:
    for line in exercise:
        line = line.replace('\n', '')
        line = line.split(" ")

        name = line[0]
        speed = int(line[3])
        time = int(line[6])
        rest = int(line[-2])
        
        reindeer = Reindeer(name, speed, time, rest)
        reindeers.append(reindeer)


for i in reindeers:
    print(i)
    print(i.trajet(2503))
