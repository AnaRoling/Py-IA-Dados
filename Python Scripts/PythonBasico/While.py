#i= 1
#while i <= 5:
    #print('*' * i)
    #i=i+1
#print("Done")

secret_number = 9
guess_cont=0
guess_limit = 3

while guess_cont < guess_limit:
    guess = int(input('Guess: '))
    guess_cont=guess_cont+1
    if guess == secret_number:
        print("You Won!")
        break
else:
    print('Sorry you failed!')


