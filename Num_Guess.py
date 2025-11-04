import random
print("   Number Guessing game:")
print("+--------------------------+")
print("Guess the number between 1-10:")
print("Total chances:3")
num=random.randint(1,10)
for i in range(3,0,-1):
    guess=int(input("Enter number:"))
    if num==guess:
        print(guess," is the guessing number congratulations 🎉🥳")
        break
    elif num>guess:
        print("too low🥹")
    else:
        print("too High😲")
    print(i-1,"chances are left")
    if i==1:
        print("you loose")