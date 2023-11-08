print("Pickling lists.\n")
print("Unpickling lists.")
import _pickle as cPickle
#variety = ["sweet", "hot", "dill"]
#variety2 = ["whole","spear","chip"]
#variety3 = ["Claussen","Heinz", "Vlassic"]

#pickle_file = open("pickles1.dat", "wb")
#cPickle.dump(variety, pickle_file)
#cPickle.dump(variety2, pickle_file)
#cPickle.dump(variety3, pickle_file)

pickle_file = open("pickles1.dat", "rb")
variety = cPickle.load(pickle_file)
shape = cPickle.load(pickle_file)
brand = cPickle.load(pickle_file)
print(variety)
print(shape)
print(brand)

import shelve
print("Shelving lists.\n")
print("Retrieving the lists from a shelved file:")
pickles = shelve.open("pickles2.dat")
pickles["variety"] = ["sweet", "hot", "dill"]
pickles["shape"] = ["whole", "spear", "chip"]
pickles["brand"] = ["Claussen", "Heinz", "Valassic"]
pickles.sync()

for key in pickles.keys():
    print(pickles[key])

print("\n\nPress the enter key to exit.")
