char = str(input("Enter a word: "))
size = len(char)
for i in range(size,0,-1):
    print(char[i-1],end = "")

