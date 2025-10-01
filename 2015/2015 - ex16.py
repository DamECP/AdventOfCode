class Aunt:

    def __init__(self, name ="", children = 0, cats = 0, samoyeds = 0, pomeranians = 0, akitas = 0, vizslas = 0, goldfish = 0, trees = 0, cars = 0, perfumes = 0):
        self.name = name
        self.children = children
        self.cats =  cats
        self.samoyeds =  samoyeds
        self.pomeranians = pomeranians
        self.akitas = akitas
        self.vizslas =  vizslas
        self.goldfish = goldfish
        self.trees = trees
        self.cars = cars
        self.perfumes = perfumes

    def compare(self, aunt):
        counter = 0
        for attribute, value in vars(self).items():
            if getattr(aunt, attribute) == value:
                counter += 1
        return self.name, counter

    def __str__(self):
        pass     

realaunt = Aunt("Sue", children = 3, cats = 7, samoyeds= 2, pomeranians= 3, akitas= 0,vizslas= 0,goldfish= 5, trees= 3, cars= 2, perfumes= 1)



with open('ex16.txt') as exercise:
    for line in exercise:
        aunt = Aunt()
        line = line.replace('\n', '')

        name = line.split(",")
        name = str(name).split(" ")[1][:-1]

        aunt.name = name
        
        line = line.split(': ')
        line = " ".join(i for i in line[1:])
        attributes = line.split(",")

        for i in attributes:
            att_val = i.strip().split(" ")
            att = att_val[0]
            val = att_val[1]
            setattr(aunt, att, val)



