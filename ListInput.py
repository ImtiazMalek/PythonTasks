#taking input and storing it
counter=input("Enter a number: "
squares = [input() for number in range(int(counter)))]
#printing it
print("Your listed names are:")
for square in squares:
    print(square)