import random
import pickle as cPickle
print("\t\tWelcome to Trivia Challenge!\n")
print("\t\tAn Episode You Can't Refuse\n\n")

problem = {}
problem[1] ={'num': 1,
            'subject': "What do you think about the ice conditions?\n",
            'content': "\t1 - Cold\n\n\t2 - Hot\n\n\t3 - Tepid\n\n\t4 - Dry\n",
            'result' : 1}
problem[2] = {'num': 2,
            'subject': "At what temperature does water boil?\n",
            'content': "\t1 - 100°C\n\n\t2 - 0°C\n\n\t3 - 50°C\n\n\t4 - 80°C\n",
            'result' : 1}
problem[3] = {'num': 3,
            'subject': "What voltage do we use at home?\n",
            'content': "\t1 - 100V\n\n\t2 - 110V\n\n\t3 - 150V\n\n\t4 - 220V\n",
            'result' : 4}

pickle_file = open("pickles1.dat", "wb")
cPickle.dump(problem[1], pickle_file)
cPickle.dump(problem[2], pickle_file)
cPickle.dump(problem[3], pickle_file)
pickle_file.close()

pickle_file = open("pickles1.dat", "rb")
choi = random.randrange(1,4)
pro = cPickle.load(pickle_file)
prob = problem[choi]
print(prob['subject'])
print(prob['content'])
try:
    anwser = int(input("What's your answer? : "))
except(ValueError):
    print("That was not a number!")

if(prob['result'] == anwser):
    print("That's correct.")
else:
    print("That's not correct.")
