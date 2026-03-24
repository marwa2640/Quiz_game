score = 0

print("Welcome to the Quiz Game!")

answer = input("1) What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2) What is 2 + 2? ")
if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3) What color is the sky? ")
if answer.lower() == "blue":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your final score is:", score)
