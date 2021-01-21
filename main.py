name = input("what is your name? ")
age = int(input("how old are you? "))

health = 10

swordDamage = 5
slelgeDamage = 3
knivesDamage = 4
damage = 0

if age >= 3:
    print("hello,", name, "you are", age, "years old")
    playGame = input("would you like to play the game? ").lower()

    if playGame == "yes" or "sure":
        print("lets play!")
        print('it was a normal day, i went to school, fell asleep during math, and played 4 square at recess, i was on my way to the bus when i heard some groaning, i looked over and saw 5 zombies! i ran off into the woods')
        print('you have', health, 'health')
        choseWeopon = input("chose your starter weopon: sword, sledge hammer, knives. ")
        if choseWeopon == 'sword':
          damage += swordDamage

        elif choseWeopon == 'sledge hammer':
          damage += slelgeDamage

        else:
          damage += knivesDamage
        
        firstChoice = input('do you want to go left or right? ')
        if firstChoice == 'left':
          print('Nice, you choose the right path. you follow the left path for a while and find a lake.')
          ans = input('do you swim across or go around? ')
          if ans == 'go around':
            print('right again! you go around and make it to the other side')
          else:
            print('you swim across and get bitten by an alligator... you lost 5 health')
            health -= 5
            print('you have', health, "health")
        else:
          print('you fell off a cliff and died')
        
else:
    print("sorry,", name, "you are not old enough to play")