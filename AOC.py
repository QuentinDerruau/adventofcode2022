class Elf:
  def __init__(self, inventory, total):
    self.inventory = inventory
    self.total= total

f = open("./puzzleInput.txt","r")
Lines = f.readlines()
count = 0
elfId= 1
inventoryElf = []
arrayElfs = []
previousValue =0
for line in Lines:
    stripLine = line.strip()
    if stripLine.strip() == "" :

        arrayElfs.append(Elf( inventoryElf, sum(inventoryElf)))

        inventoryElf = []
    else :
        inventoryElf.append(int(stripLine))
    count += 1 
    arrayElfs.sort(key=lambda x: x.total, reverse=True)
print(arrayElfs[0].total + arrayElfs[1].total + arrayElfs[2].total)
