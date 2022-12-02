f = open("./input.txt", "r")
Lines = f.readlines()
player1 = 0


conditionLoose = [ "A Z", "B X", "C Y" ]
conditionDraw = [ "A X","B Y","C Z" ]  
conditionWin = [ "A Y", "B Z", "C X" ]

def checkSituation(input):
    if input in conditionWin : return 6
    elif input in conditionDraw : return 3
    elif input in conditionLoose : return 0
def checkSign(input):
    value = 0
    if input == "X":
      value = 1
    elif input == "Y":
      value = 2
    elif input == "Z":
      value = 3
    return value
    
    
for line in Lines:
    stripLine = line.strip()
    player1 += checkSituation(stripLine) + checkSign(stripLine[2])
    print(stripLine, checkSign(stripLine[2]), checkSituation(stripLine), player1)
    
print(player1)