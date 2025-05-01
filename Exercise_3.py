# Create a program capable of displaying  questiond to the user like KBC
# Use List data type to store the questions and answers.
# Display the final amount the person is taking home after playing the game.

print("Let's play KBC!")
question = ("The capital of India is?", "The capital of USA is?", "The capital of France is?")
options = (("Delhi", "Mumbai", "Chennai", "Kolkata"), ("Washington DC", "New York", "Los Angeles", "Chicago"), ("Paris", "London", "Berlin", "Madrid"))
print(question[0])
print("1. ", options[0][0])
print("2. ", options[0][1])
print("3. ", options[0][2])
print("4. ", options[0][3])
answer = input("Enter your answer: ")

if answer == "1":
    print("Correct!")
    print("You have won 1,000,000!")
else:
    print("Wrong answer!")
    print("Game Over!")
    exit()


print(question[1])    
print("1. ", options[1][0])
print("2. ", options[1][1])
print("3. ", options[1][2])
print("4. ", options[1][3])
answer = input("Enter your answer: ")
if answer == "1":
    print("Correct!")
    print("You have won 2,000,000!")
else:
    print("Wrong answer!")
    print("Game Over!")
    exit()


print(question[2])
print("1. ",options[2][0])
print("2. ",options[2][1])
print("3. ",options[2][2])
print("4. ",options[2][3])
answer = input("Enter your answer: ")
if answer == "1":
    print("Correct!")
    print("You have won 3,000,000!") 
else:
    print("Wrong answer!")
    print("Game Over!")
    exit()

print("Congratulations! You have won the game!")


