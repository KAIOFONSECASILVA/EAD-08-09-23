a= int (input("digite o primeiro valor:"))
b= int (input("digite o segundo valor:"))
print("1)soma:")
print("2)sub:")
print("3)mult:")
print("4)div")

op=(input("De sua escolha: "))
if op=="1":
  print(a+b)
elif op=="2":
  print(a-b)
elif op=="3":
  print(a*b)
elif op=="4":
  print(a/b)