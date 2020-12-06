x = float(input("Podaj 1 liczbe: "))
y = float(input("Podaj 2 liczbe: "))
znak = input("Podaj działanie: ")
#kalkulator
#xD
if znak == "+":
    print(x + y)
elif znak == "-":
    print(x - y)
elif znak == "*":
    print(x*y)
elif znak == "/":
    print(x/y)
else:
    print("Błąd")
