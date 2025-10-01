with open("ex6.txt") as exercise:
    data = exercise.readlines()
    data = [i.strip() for i in data]


class Light:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.brightness = 0

    def on(self):
        self.brightness += 1

    def off(self):
        if self.brightness > 0:
            self.brightness -= 1

    def toggle(self):
        self.brightness += 2


lights = {}
for x in range(1000):
    for y in range(1000):
        l = Light(x, y)
        lights[(x, y)] = l

for instruction in data:
    inst = instruction.split(",")
    start_x = int(inst[0].split(" ")[-1])
    end_x = int(inst[1].split(" ")[-1])
    start_y = int(inst[1].split(" ")[0])
    end_y = int(inst[-1])

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            light = lights[(x, y)]
            if "on" in inst[0]:
                light.on()
            elif "off" in inst[0]:
                light.off()
            elif "toggle" in inst[0]:
                light.toggle()

score = 0
for key, value in lights.items():
    score += value.brightness

print(score)
