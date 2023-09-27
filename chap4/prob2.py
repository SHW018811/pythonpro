import random

heroHP = random.randrange(50, 101)
monsterHP = random.randrange(50,101)
herostat = ""
monststat = ""
count = 0
print("hero HP:",heroHP,"monster HP:",monsterHP)

while True:
    heroAtk = random.randrange(-10,21)
    monsterAtk = random.randrange(-10,21)
    if heroAtk > 0 :
        herostat = "success"
        monsterHP -= heroAtk
    else:
        herostat = "fail"
    if monsterAtk > 0:
        monststat = "success"
        heroHP -= monsterAtk
    else:
        monststat = "fail"
    print("hero(HP:",heroHP,", attack:",heroAtk,") ",herostat," <-> monster(HP:",monsterHP,", attack:",monsterAtk,") ",monststat,sep='')
    count+=1
    if heroHP < 0 or monsterHP < 0: break

print("-----------------------------------------------------------")
print("Total phase:",count)
if monsterHP > 0:
    print("Monster Win!!!!")
else:
    print("Hero Win!!!!")
