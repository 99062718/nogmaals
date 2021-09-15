dagen = ["ma", "di", "wo", "do", "vr", "za", "zo"]
userInput = input("vul hier een dag in: ")
x = 0

while x <= dagen.index(userInput):
    print(dagen[x])
    x += 1