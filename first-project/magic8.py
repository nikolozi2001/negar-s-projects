import random
import time

name = "Nika"

question = "Will I win the lottery?"

answer = ""

randomNumber = random.randint(1, 9)

if randomNumber == 1:
    print('Yes - definitely.')
elif randomNumber == 2:
    print("It is decidedly so.")
elif randomNumber == 3:
    print("Without a doubt.")
elif randomNumber == 4:
    print("Reply hazy, try again.")
elif randomNumber == 5:
    print("Ask again later.")
elif randomNumber == 6:
    print("Better not tell you now.")
elif randomNumber == 7:
    print("My sources say no.")
elif randomNumber == 8:
    print("Outlook not so good.")
elif randomNumber == 9:
    print("Very doubtful.")
else:
    answer = "Error"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)

time.sleep(2)
