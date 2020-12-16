#code by PyJavaPulver 2020
from list import list_1
from list import list_2
print('Casio Test Terminal')

def ini():
  start = input("test> ")
  if start == "h":
    num = 0
    for x in list_1:
        num = num + 1
        string = str(num) + '. ' + x
        print(string)
    #print(num)
  elif start == "e":
    print("exiting...")
    raise SystemExit

  elif start.isdigit():
    if int(start) <= len(list_1):
        print(list_1[int(start)-1]+":\n"+list_2[int(start)-1])
    else:
        print('not found')
  ini()
ini()
