import random
print("Welcome to Hogwarts now you have to choose your Room")
rooms = ["Gryffindor", "Slytherin"," Raenclaw", "Hufflepuff"]
print(r'''
                    __
                   /  \
                  /    \
                 /      \
                /        \
               /          \
              /            \
             /              \
            /                \
           /                  \
          /                    \
         /                      \
        /                        \
       /__________________________\
      /                            \
     /                              \
    /________________________________\
''')
your_room = random.choice(rooms)
print(f"you so hard intelegant and brave you will jon to  {your_room}")
print("nok nock Harry do you her sound come from the path ")
choose_1 = input("you will go or not  type go  or wait: \n").lower()
if choose_1 == "go":
    print("you here sound snake come from . and found the cat frozen ")
    choose_2 = input("choose the mascot to make a cat walk a gain : type one for the first or two  \n").lower()
    if choose_2 == "one":
        print("Deletrius\n you make a  cat move agin thanks Harry")
        print("Harry there is a huge snake in the path, herry")
        choose_3 = input("in Path you Found Snak and Lord Voldemort which mascot you will use : wite one or two\n").lower()
        if choose_3 == "two":
            print("Petrificus Totalus \n thanks harry we will call  professor Dumbledore you stop the bad guy")
            print(r'''
                 ,/   *
              _,'/_   |
              `(")' ,'/
           _ _,-H-./ /
           \_\_\.   /
             )" |  (
          __/   H   \__
          \    /|\    /
           `--'|||`--'
              ==^==
            ''')
        elif choose_3 == "one":
            print("Silencio \n oh harry snake will attach you . Game over")
    elif choose_2 == "two":
        print("Incendio\n thanks harry the cat in fire go back home.\n Game Over")
elif choose_1 == "wait":
    print("Sorry harry you will not brave enough. \nGame Over")
else:
    print("Game Over")