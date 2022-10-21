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
    score = score + 1
    print(f"Your score is currently {score}")
else:
    print("I'm sorry that's incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == 'graphics processing unit':
    print("Yes! That's correct")
else:
    print("I'm sorry that's incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    print("Yes! That's correct")
else:
    print("I'm sorry that's incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == 'power supply unit':
    print("Yes! That's correct")
else:
    print("I'm sorry that's incorrect")
