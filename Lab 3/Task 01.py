with open('zaid.txt', 'w') as file:
    sentence = input("Enter your sentence: ")
    file.write(sentence)


with open('zaid.txt', 'r') as file:
    content = file.read()
print(content)

number_of_words = 0

with open('zaid.txt', 'r') as file:
    data = file.read()
lines = data.split()
number_of_words = number_of_words + len(lines)
print(number_of_words)

