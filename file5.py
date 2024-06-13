
'''5. Write a program that takes a string input from the user and writes it to a
text file.'''


text = input("Enter a string: ")


with open("output.txt", "w") as file:
    file.write(text)

print("String has been written to output.txt")
