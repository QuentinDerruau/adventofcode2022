class Elf:
  def __init__(self, inventory):
    self.inventory = inventory

f = open("./puzzleInput.txt","r")
Lines = f.readlines()
count = 0
elfId= 1
inventoryElf = []
arrayElfs = [Elf]
higherElf=0
previousValue =0
for line in Lines:
    stripLine = line.strip()
    if stripLine.strip() == "" :
        arrayElfs.append(Elf( inventoryElf))
        inventoryElf = []
    else :
        inventoryElf.append(int(stripLine))
    count += 1 
    for i in range(len(arrayElfs)-1):
        actualValue = sum(arrayElfs[i+1].inventory)
        if previousValue < actualValue :
            previousValue = actualValue
            higherElf = i+1
print(sum(arrayElfs[higherElf].inventory))

