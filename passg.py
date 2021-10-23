import random

try:
    passwdLen = int(input("Enter password length: "))
    if passwdLen <= 0:
        print("\n[SYSTEM] Please enter a number bigger than 0!")
except ValueError:
    print("\n[SYSTEM] Please enter number!")
    exit()

password = []

for i in range(0,passwdLen):
    data = random.randint(1,36)
    if data == 1:
        if random.randint(1,2) == 1:
            password.append("a")
        else:
            password.append("A")

    elif data == 2:
        if random.randint(1,2) == 1:
            password.append("b")
        else:
            password.append("B")
        
    elif data == 3:
        if random.randint(1,2) == 1:
            password.append("c")
        else:
            password.append("C")

    elif data == 4:
        if random.randint(1,2) == 1:
            password.append("d")
        else:
            password.append("D")

    elif data == 5:
        if random.randint(1,2) == 1:
            password.append("e")
        else:
            password.append("E")
    
    elif data == 6:
        if random.randint(1,2) == 1:
            password.append("f")
        else:
            password.append("F")

    elif data == 7:
        if random.randint(1,2) == 1:
            password.append("g")
        else:
            password.append("G")

    elif data == 8:
        if random.randint(1,2) == 1:
            password.append("h")
        else:
            password.append("H")

    elif data == 9:
        if random.randint(1,2) == 1:
            password.append("i")
        else:
            password.append("I")

    elif data == 10:
        if random.randint(1,2) == 1:
            password.append("j")
        else:
            password.append("J")

    elif data == 11:
        if random.randint(1,2) == 1:
            password.append("k")
        else:
            password.append("K")

    elif data == 12:
        if random.randint(1,2) == 1:
            password.append("l")
        else:
            password.append("L")

    elif data == 13:
        if random.randint(1,2) == 1:
            password.append("m")
        else:
            password.append("M")

    elif data == 14:
        if random.randint(1,2) == 1:
            password.append("n")
        else:
            password.append("N")

    elif data == 15:
        if random.randint(1,2) == 1:
            password.append("o")
        else:
            password.append("O")

    elif data == 16:
        if random.randint(1,2) == 1:
            password.append("p")
        else:
            password.append("P")

    elif data == 17:
        if random.randint(1,2) == 1:
            password.append("r")
        else:
            password.append("R")

    elif data == 18:
        if random.randint(1,2) == 1:
            password.append("s")
        else:
            password.append("S")

    elif data == 19:
        if random.randint(1,2) == 1:
            password.append("t")
        else:
            password.append("T")
    
    elif data == 20:
        if random.randint(1,2) == 1:
            password.append("u")
        else:
            password.append("U")

    elif data == 21:
        if random.randint(1,2) == 1:
            password.append("v")
        else:
            password.append("V")

    elif data == 22:
        if random.randint(1,2) == 1:
            password.append("y")
        else:
            password.append("Y")

    elif data == 23:
        if random.randint(1,2) == 1:
            password.append("z")
        else:
            password.append("Z")

    elif data == 24:
        if random.randint(1,2) == 1:
            password.append("q")
        else:
            password.append("Q")

    elif data == 25:
        if random.randint(1,2) == 1:
            password.append("w")
        else:
            password.append("W")

    elif data == 26:
        if random.randint(1,2) == 1:
            password.append("x")
        else:
            password.append("X")

    elif data == 27:
        password.append("0")
    
    elif data == 28:
        password.append("1")

    elif data == 29:
        password.append("2")

    elif data == 30:
        password.append("3")

    elif data == 31:
        password.append("4")

    elif data == 32:
        password.append("5")

    elif data == 33:
        password.append("6")

    elif data == 34:
        password.append("7")

    elif data == 35:
        password.append("8")

    elif data == 36:
        password.append("9")

string_password = ""
for i in range(0,passwdLen):
    string_password = string_password + str(password[i])

print(string_password)