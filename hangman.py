counter8 = 0
first = ["""





===============
"""]
w = (', '.join(first))

second = ["""
    |
    |
    |
    |
    |
    |
    |
    |
    |
========================
"""]

b = (', '.join(second))



third = ["""
    +-----------+
    |  
    | 
    |
    |
    |
    |
    |
    |
    |
========================
"""]

a = (', '.join(third))


fourth = ["""
    +-----------+
    |           O
    |
    |
    |
    |
    |
    |
    |
    |
========================
"""]

p = (', '.join(fourth))


fith = ["""
    +-----------+
    |           O
    |           +
    |           |
    |
    |
    |
    |
    |
    |
========================
"""]

t = (', '.join(fith))





sixth = ["""
    +-----------+
    |           O
    |        ---+
    |           |
    |
    |
    |
    |
    |
    |
========================
"""]

l = (', '.join(sixth))

seven = ["""
    +-----------+
    |           O
    |        ---+---
    |           |
    |
    |
    |
    |
    |
    |
========================
"""]

y = (', '.join(seven))


eigth = ["""
    +-----------+
    |           O
    |        ---+---
    |           |
    |          / 
    |         /   
    |        /     
    |
    |
    |
========================
"""]

x = (', '.join(eigth))

nine = ["""
    +-------
    |       o
    |    ---+---
    |       |
    |      / \   
    |     /   \  
    |    /     \    
    |     
=====================
    """]

z = (', '.join(nine))
while True:
    print("\n\nWelcome to hangman!\n===================")
    import random
    topic = random.randint(1,3)
    if topic == 1 :
        print("\nYour topic is animals")
        array = ["bee" , "cat" , "dog" , "fish" , "kangaroo" , "bear" , "shark" , "alpaca" , "sheep" , "cow" , "otter" , "lion" , "spider" , "snake" , "snail" , "rhino" , "octopus" , "cheetah" , "pony"]
    elif topic == 2 :
        print("\nYour topic is movies!")
        array = ["submarine" , "goodfellas" , "se7en" , "shrek" , "up" , "babe" , "bambi" , "dumbo" , "ciderella" , "hotfuzz" , "pinocchio" , "cars" , "octopussy" , "underdog" , "valiant" , "garfield" , "holes" , "dinosaur" , "alladin"] 
    elif topic == 3 :
        print("\nYour topic is shops")
        array = ["tesco" , "sainsburys" , "halfords" , "waitroes" , "asda" , "morrisons" , "spar" , "londis" , "currys" , "comet" , "millets" , "safeway" , "argos" , "primark" , "waterstones" , "ottokars" , "somerfield" , "co-operative" , "topshop"]
    position = random.randint(0,18)
    word = array[position]
    leng = len(word)
    aguess = (leng + 10)
    amount = 0
    string = []
    counter2 = 0
    c = 0
    counter4 = 0
    counter5 = 1
    counter6 = 0
    counter8 = 0
    array17 = []
    counter22 = 0
    q = '_'
    while amount != leng:
        amount += 1
        string.append(q)
    print('   '.join(string))
    while c == 0:
        left = 9 - counter8
        print("\nYou have" , left , "guesses remaining!")
        guess = input("\n\nEnter a letter : ").lower()
        counter6 += 1
        array17.append(guess)
        print(end="\nLetters you have used so far: ")
        print(' '.join(array17) , "\n")
        while counter2 != leng: 
            if guess == word[counter2]:
                print("\nThat is in the word! Well done!\n")
                string[counter2]= guess
                counter2 += 1
                while counter4 != leng :
                    if string[counter4] != '_':
                        counter4 += 1
                        counter5 += 1
                    else:
                        counter4 += 1
                    if counter5 == leng:
                        print('\nWell done! You got it!\n')
                        c = 1
                        break
                    else:
                        c = 0
            else:
                counter2 += 1
                counter22 += 1
        if counter22 == leng :
            counter8 += 1
        if counter8 == 1:
            print(w)
        elif counter8 == 2:
            print(b)
        elif counter8 == 3:
            print(a)
        elif counter8 == 4:
            print(p)
        elif counter8 == 5:
            print(t)
        elif counter8 == 6:
            print(l)
        elif counter8 == 7:
            print(y)
        elif counter8 == 8:
            print(x)
        elif counter8 == 9:
            print(z)
                
        print('   '.join(string))
        if c == 1:
            print("\nYOU GOT IT!!!")
        if counter8 == int(9) :
            print("\n\nYou ran out of guesses!")
            print("\nThe word was" , word)
            break
        counter2 = 0
        counter4 = 0
        counter5 = 0
        counter22 = 0




















































































