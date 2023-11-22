class Critter:
    def __init__(self, name, moodlevel):
        self.name = name
        self.Mood_level = moodlevel
    def Talk(self):
        if self.Mood_level >= 4:
            print(self.name,"feels the best.")
        elif self.Mood_level == 3:
            print(self.name,"feels good.")
        elif self.Mood_level == 2:
            print(self.name,"is feeling so-so")
        elif self.Mood_level == 1:
            print(self.name,"is not in a good mood.")
        else :
            print(self.name,"is in the worst mood.")
        print()
        #기분 레벨에 따라 말하고 말할때 마다 기분 레벨 하강
    def Feed(self):
        #먹이를 먹음, 기분 레벨 상승
        print("After I fed",self.name,",",self.name,"felt better.\n")
        print("Mood Level :",self.Mood_level)
    def Play(self):
        #주인과 놀이, 기분 레벨 상승
        print(self.name,"felt good after playing with his owner.\n")
        print("Mood Level :",self.Mood_level)
    def setMood(self, level):
        #기분레벨 설정
        self.Mood_level = level
    def getMood(self):
        #기분레벨 반환
        print("Mood Level :", self.Mood_level,"\n")

class Snack:
    def __init__(self, name, Level):
        self.name = name
        self.Level = Level
    def getLevel(self,name):
        return name.Level
    def setCritterLevel(self,critter):
        critter.setMood(crit.Mood_level+self.Level)


name = input("What do you want to name your critter? : ")
snk1 = Snack("Rice",1)
snk2 = Snack("Feed", 3)
snk3 = Snack("Steak", 5)

crit = Critter(name, 4)
while True:
    print()
    print("\tCritter Garetaker\n")
    print("\t0 - Quit")
    print("\t1 - Listen to your critter")
    print("\t2 - Feed your critter")
    print("\t3 - Play with your critter\n")
    su = int(input("Choice: "))
    if su == 0 : break
    elif su == 1:
        crit.Talk()
        crit.setMood(crit.Mood_level-1)
    elif su == 2:
        print("Choose what food to feed",crit.name,".")
        print("1 -",snk1.name)
        print("2 -",snk2.name)
        print("3 -",snk3.name,"\n")
        sel = int(input("Choise : "))
        if sel == 1:
            crit.setMood(crit.Mood_level+snk1.Level)
            print(crit.name,"eat",snk1.name)
        elif sel == 2:
            crit.setMood(crit.Mood_level+snk2.Level)
            print(crit.name,"eat",snk2.name)
        elif sel == 3:
            crit.setMood(crit.Mood_level+snk3.Level)
            print(crit.name,"eat",snk3.name)
        crit.Feed()
    elif su == 3:
        crit.setMood(crit.Mood_level+2)
        crit.Play()
