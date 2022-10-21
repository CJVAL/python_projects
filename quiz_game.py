from tkinter.messagebox import YES


print("Welcome to my computer quiz!")

playing = input("Would you like to play? ")
if playing.lower() != 'yes':
    quit()

print("Okay, let's play!")
score = 0
print(f"Your score is currently {score}")

answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print("Yes! That's correct")
    score += 1
    #score(f"Your score is currently {score}")
else:
    print("I'm sorry that's incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == 'graphics processing unit':
    print("Yes! That's correct")
    score += 1
else:
    print("I'm sorry that's incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    print("Yes! That's correct")
    score += 1
else:
    print("I'm sorry that's incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == 'power supply unit':
    print("Yes! That's correct")
    score += 1
else:
    print("I'm sorry that's incorrect")

print(f"You have reached the end of the quiz. \nYour score was {score}")
print(f"You got {score/4*100}% correct")