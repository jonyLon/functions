import random
print(" 1 ", chr(9474)," 2 ", chr(9474)," 3 ",chr(9474), " 4 ", chr(9474), " 5 ",sep="")
print(chr(9472)*3, chr(9532),chr(9472)*3,chr(9532),chr(9472)*3, chr(9532), chr(9472)*3,chr(9532), chr(9472)*3,sep="")
print(" 6 ", chr(9474)," 7 ", chr(9474)," 8 ",chr(9474), " 9 ", chr(9474), " 10",sep="")
print(chr(9472)*3, chr(9532),chr(9472)*3,chr(9532),chr(9472)*3, chr(9532), chr(9472)*3,chr(9532), chr(9472)*3,sep="")
print(" 11", chr(9474)," 12", chr(9474)," 13",chr(9474), " 14", chr(9474), " 15",sep="")
print(chr(9472)*3, chr(9532),chr(9472)*3,chr(9532),chr(9472)*3, chr(9532), chr(9472)*3,chr(9532), chr(9472)*3,sep="")
print(" 16", chr(9474)," 17", chr(9474)," 18",chr(9474), " 19", chr(9474), " 20",sep="")
print(chr(9472)*3, chr(9532),chr(9472)*3,chr(9532),chr(9472)*3, chr(9532), chr(9472)*3,chr(9532), chr(9472)*3,sep="")
print(" 21", chr(9474)," 22", chr(9474)," 23",chr(9474), " 24", chr(9474), " 25",sep="")
print()


def showSymbol(s,symbol):
  match s:
    case 1:
      if list[0][0] == "   ":
        list[0][0] = symbol
    case 2:
      if list[0][1] == "   ":
        list[0][1] = symbol     
    case 3:
      if list[0][2] == "   ":
        list[0][2] = symbol     
    case 4:
      if list[0][3] == "   ":
        list[0][3] = symbol     
    case 5:
      if list[0][4] == "   ":
        list[0][4] = symbol     
    case 6:
      if list[1][0] == "   ":
        list[1][0] = symbol     
    case 7:
      if list[1][1] == "   ":
        list[1][1] = symbol     
    case 8:
      if list[1][2] == "   ":
        list[1][2] = symbol     
    case 9:
      if list[1][3] == "   ":
        list[1][3] = symbol
    case 10:
      if list[1][4] == "   ":
        list[1][4] = symbol     
    case 11:
      if list[2][0] == "   ":
        list[2][0] = symbol     
    case 12:
      if list[2][1] == "   ":
        list[2][1] = symbol     
    case 13:
      if list[2][2] == "   ":
        list[2][2] = symbol     
    case 14:
      if list[2][3] == "   ":
        list[2][3] = symbol     
    case 15:
      if list[2][4] == "   ":
        list[2][4] = symbol     
    case 16:
      if list[3][0] == "   ":
        list[3][0] = symbol     
    case 17:
      if list[3][1] == "   ":
        list[3][1] = symbol     
    case 18:
      if list[3][2] == "   ":
        list[3][2] = symbol
    case 19:
      if list[3][3] == "   ":
        list[3][3] = symbol     
    case 20:
      if list[3][4] == "   ":
        list[3][4] = symbol     
    case 21:
      if list[4][0] == "   ":
        list[4][0] = symbol     
    case 22:
      if list[4][1] == "   ":
        list[4][1] = symbol     
    case 23:
      if list[4][2] == "   ":
        list[4][2] = symbol     
    case 24:
      if list[4][3] == "   ":
        list[4][3] = symbol
    case 25:
      if list[4][4] == "   ":
        list[4][4] = symbol      


def showField():
  print(list[0][0], chr(9474),list[0][1], chr(9474),list[0][2],chr(9474), list[0][3], chr(9474), list[0][4],sep="")
  print(chr(9472)*3, chr(9532),chr(9472)*3,chr(9532),chr(9472)*3, chr(9532), chr(9472)*3,chr(9532), chr(9472)*3,sep="")
  print(list[1][0], chr(9474),list[1][1], chr(9474),list[1][2],chr(9474), list[1][3], chr(9474), list[1][4],sep="")
  print(chr(9472)*3, chr(9532),chr(9472)*3,chr(9532),chr(9472)*3, chr(9532), chr(9472)*3,chr(9532), chr(9472)*3,sep="")
  print(list[2][0], chr(9474),list[2][1], chr(9474),list[2][2],chr(9474), list[2][3], chr(9474), list[2][4],sep="")
  print(chr(9472)*3, chr(9532),chr(9472)*3,chr(9532),chr(9472)*3, chr(9532), chr(9472)*3,chr(9532), chr(9472)*3,sep="")
  print(list[3][0], chr(9474),list[3][1], chr(9474),list[3][2],chr(9474), list[3][3], chr(9474), list[3][4],sep="")
  print(chr(9472)*3, chr(9532),chr(9472)*3,chr(9532),chr(9472)*3, chr(9532), chr(9472)*3,chr(9532), chr(9472)*3,sep="")
  print(list[4][0], chr(9474),list[4][1], chr(9474),list[4][2],chr(9474), list[4][3], chr(9474), list[4][4],sep="")
  print()
def isVictory(s):
  if list[0][0] == s and list[0][1] == s and list[0][2] == s and list[0][3] == s and list[0][4] == s or list[1][0] == s and list[1][1] == s and list[1][2] == s and list[1][3] == s and list[1][4] == s or list[2][0] == s and list[2][1] == s and list[2][2] == s and list[2][3] == s and list[2][4] == s or list[3][0] == s and list[3][1] == s and list[3][2] == s and list[3][3] == s and list[3][4] == s or list[4][0] == s and list[4][1] == s and list[4][2] == s and list[4][3] == s and list[4][4] == s or list[0][0] == s and list[1][0] == s and list[2][0] == s and list[3][0] == s and list[4][0] == s or list[0][1] == s and list[1][1] == s and list[2][1] == s and list[3][1] == s and list[4][1] == s or list[0][2] == s and list[1][2] == s and list[2][2] == s and list[3][2] == s and list[4][2] == s or list[0][3] == s and list[1][3] == s and list[2][3] == s and list[3][3] == s and list[4][3] == s or list[0][4] == s and list[1][4] == s and list[2][4] == s and list[3][4] == s and list[4][4] == s or list[0][0] == s and list[1][1] == s and list[2][2] == s and list[3][3] == s and list[4][4] == s or list[0][4] == s and list[1][3] == s and list[2][2] == s and list[3][1] == s and list[4][0] == s:
    return True
  else:
    return False
  
def isFullField():
    if list[0].count("   ") == 0 and list[1].count("   ") == 0 and list[2].count("   ") == 0 and list[3].count("   ") == 0 and list[4].count("   ") == 0:
      return True
    else:
      return False
def template(a):
  return " "+str(a)+" "

def botLogic(user_symb,bot_symb):
  if list[0].count(user_symb) == 4 and list[0].index("   ") > 0:
    i = list[0].index("   ")
    list[0][i] = bot_symb
  if list[1].count(user_symb) == 4 and list[1].count("   ") > 0:
    i = list[1].index("   ")
    list[1][i] = bot_symb
  if list[2].count(user_symb) == 4 and list[2].count("   ") > 0:
    i = list[2].index("   ")
    list[2][i] = bot_symb
  if list[3].count(user_symb) == 4 and list[3].count("   ") > 0:
    i = list[3].index("   ")
    list[3][i] = bot_symb
  if list[4].count(user_symb) == 4 and list[4].count("   ") > 0:
    i = list[4].index("   ")
    list[4][i] = bot_symb
  if list[0][0] != user_symb and list[1][0] == user_symb and list[2][0] == user_symb and list[3][0] == user_symb and list[4][0] == user_symb:
    list[0][0] = bot_symb
  if list[0][0] == user_symb and list[1][0] != user_symb and list[2][0] == user_symb and list[3][0] == user_symb and list[4][0] == user_symb:
    list[1][0] = bot_symb
  if list[0][0] == user_symb and list[1][0] == user_symb and list[2][0] != user_symb and list[3][0] == user_symb and list[4][0] == user_symb:
    list[2][0] = bot_symb
  if list[0][0] == user_symb and list[1][0] == user_symb and list[2][0] == user_symb and list[3][0] != user_symb and list[4][0] == user_symb:
    list[3][0] = bot_symb
  if list[0][0] == user_symb and list[1][0] == user_symb and list[2][0] == user_symb and list[3][0] == user_symb and list[4][0] != user_symb:
    list[4][0] = bot_symb
  if list[0][1] != user_symb and list[1][1] == user_symb and list[2][1] == user_symb and list[3][1] == user_symb and list[4][1] == user_symb:
    list[0][1] = bot_symb
  if list[0][1] == user_symb and list[1][1] != user_symb and list[2][1] == user_symb and list[3][1] == user_symb and list[4][1] == user_symb:
    list[1][1] = bot_symb
  if list[0][1] == user_symb and list[1][1] == user_symb and list[2][1] != user_symb and list[3][1] == user_symb and list[4][1] == user_symb:
    list[2][1] = bot_symb
  if list[0][1] == user_symb and list[1][1] == user_symb and list[2][1] == user_symb and list[3][1] != user_symb and list[4][1] == user_symb:
    list[3][1] = bot_symb
  if list[0][1] == user_symb and list[1][1] == user_symb and list[2][1] == user_symb and list[3][1] == user_symb and list[4][1] != user_symb:
    list[4][1] = bot_symb
  if list[0][2] != user_symb and list[1][2] == user_symb and list[2][2] == user_symb and list[3][2] == user_symb and list[4][2] == user_symb:
    list[0][2] = bot_symb
  if list[0][2] == user_symb and list[1][2] != user_symb and list[2][2] == user_symb and list[3][2] == user_symb and list[4][2] == user_symb:
    list[1][2] = bot_symb
  if list[0][2] == user_symb and list[1][2] == user_symb and list[2][2] != user_symb and list[3][2] == user_symb and list[4][2] == user_symb:
    list[2][2] = bot_symb
  if list[0][2] == user_symb and list[1][2] == user_symb and list[2][2] == user_symb and list[3][2] != user_symb and list[4][2] == user_symb:
    list[3][2] = bot_symb
  if list[0][2] == user_symb and list[1][2] == user_symb and list[2][2] == user_symb and list[3][2] == user_symb and list[4][2] != user_symb:
    list[4][2] = bot_symb
  if list[0][3] != user_symb and list[1][3] == user_symb and list[2][3] == user_symb and list[3][3] == user_symb and list[4][3] == user_symb:
    list[0][3] = bot_symb
  if list[0][3] == user_symb and list[1][3] != user_symb and list[2][3] == user_symb and list[3][3] == user_symb and list[4][3] == user_symb:
    list[1][3] = bot_symb
  if list[0][3] == user_symb and list[1][3] == user_symb and list[2][3] != user_symb and list[3][3] == user_symb and list[4][3] == user_symb:
    list[2][3] = bot_symb
  if list[0][3] == user_symb and list[1][3] == user_symb and list[2][3] == user_symb and list[3][3] != user_symb and list[4][3] == user_symb:
    list[3][3] = bot_symb
  if list[0][3] == user_symb and list[1][3] == user_symb and list[2][3] == user_symb and list[3][3] == user_symb and list[4][3] != user_symb:
    list[4][3] = bot_symb
  if list[0][4] != user_symb and list[1][4] == user_symb and list[2][4] == user_symb and list[3][4] == user_symb and list[4][4] == user_symb:
    list[0][4] = bot_symb
  if list[0][4] == user_symb and list[1][4] != user_symb and list[2][4] == user_symb and list[3][4] == user_symb and list[4][4] == user_symb:
    list[1][4] = bot_symb
  if list[0][4] == user_symb and list[1][4] == user_symb and list[2][4] != user_symb and list[3][4] == user_symb and list[4][4] == user_symb:
    list[2][4] = bot_symb
  if list[0][4] == user_symb and list[1][4] == user_symb and list[2][4] == user_symb and list[3][4] != user_symb and list[4][4] == user_symb:
    list[3][4] = bot_symb
  if list[0][4] == user_symb and list[1][4] == user_symb and list[2][4] == user_symb and list[3][4] == user_symb and list[4][4] != user_symb:
    list[4][4] = bot_symb
  if list[0][4] != user_symb and list[1][3] == user_symb and list[2][2] == user_symb and list[3][1] == user_symb and list[4][0] == user_symb:
    list[0][4] = bot_symb
  if list[0][4] == user_symb and list[1][3] != user_symb and list[2][2] == user_symb and list[3][1] == user_symb and list[4][0] == user_symb:
    list[1][3] = bot_symb
  if list[0][4] == user_symb and list[1][3] == user_symb and list[2][2] != user_symb and list[3][1] == user_symb and list[4][0] == user_symb:
    list[2][2] = bot_symb
  if list[0][4] == user_symb and list[1][3] == user_symb and list[2][2] == user_symb and list[3][1] != user_symb and list[4][0] == user_symb:
    list[3][1] = bot_symb
  if list[0][4] == user_symb and list[1][3] == user_symb and list[2][2] == user_symb and list[3][1] == user_symb and list[4][0] != user_symb:
    list[4][0] = bot_symb
  if list[0][0] != user_symb and list[1][1] == user_symb and list[2][2] == user_symb and list[3][3] == user_symb and list[4][4] == user_symb:
    list[0][0] = bot_symb
  if list[0][0] == user_symb and list[1][1] != user_symb and list[2][2] == user_symb and list[3][3] == user_symb and list[4][4] == user_symb:
    list[1][1] = bot_symb
  if list[0][0] == user_symb and list[1][1] == user_symb and list[2][2] != user_symb and list[3][3] == user_symb and list[4][4] == user_symb:
    list[2][2] = bot_symb
  if list[0][0] == user_symb and list[1][1] == user_symb and list[2][2] == user_symb and list[3][3] != user_symb and list[4][4] == user_symb:
    list[3][3] = bot_symb
  if list[0][0] == user_symb and list[1][1] == user_symb and list[2][2] == user_symb and list[3][3] == user_symb and list[4][4] != user_symb:
    list[4][4] = bot_symb
  showSymbol(random.randint(1,25),bot_symb)

workflow = True
while workflow:
  list = [["   " for i in range(5)] for i in range(5)]
  symbol = input("Enter preferable symbol(0 or X): ")
  if symbol == "0":
    botSymbol = "X"
  elif symbol == "X":
    botSymbol = "0"
  else:
    print("Error: invalid symbol")
    break
  templateUser = template(symbol)
  templateBot = template(botSymbol)
  while True:
    user = int(input("Enter number of cell: "))
    showSymbol(user,templateUser)
    showField()
    botLogic(templateUser,templateBot)
    showField()
    if isVictory(templateUser):
      print("You win!")
      break
    if isVictory(templateBot):
      print("You lose!")
      break
    if isFullField():
      showField()
      print("Draw!")
      break
  again = int(input("Play again? (1 - yes, 2 - no): "))
  if again == 1:
    workflow = True
  elif again == 2:
    workflow = False
  else:
    print("Error: invalid input")
    workflow = False