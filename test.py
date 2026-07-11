import random

names = ["Alice", "Bob", "Charlie", "David"]
random.shuffle(names)


# wirte code here

for name in names:
    if name == "David":
        print(name)
    
names.append(1, "Ayo")
