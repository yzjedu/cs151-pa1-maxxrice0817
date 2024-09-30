# Max Rice PA01
name = input("Enter your name: ")
miles_traveled = float(input(f" How many miles will you travel?: "))
if miles_traveled <= 5.5:
    location = ('Rockville')
    print(f'{name} has arrived in Rockville')
if miles_traveled >5.5 and miles_traveled < 100:
    location = ('Forest')
    print(f'{name} has arrived in the Forest')
elif miles_traveled >= 100:
    location = ('end of the world')
    print('GAME OVER: That is a little long for a walk, why dont you go somewhere closer')

#Rockville story line
if location=='Rockville':
    artifact = (input(f"Steve: Hello {name} I am the local trader Steve, would you like to you an artifact, yes or no?: "))
    if artifact=='yes':
        amount_money = int(input('Steve: How many dollars do you have? '))
        if amount_money < 50:
            print('Steve: Are you joking! go home and do not return until you have some real money')
            print('GAME OVER: you went home empty handed')
        if amount_money >= 50:
            print('Steve: How lucky! That’s exactly how much it costs, pleasure doing business I guess we both better start heading home!')
            print('GAME OVER: You went Home broke')
    if artifact=='no':
        print('If you’re not buying you better just head home!')
        print('GAME OVER: you went home empty handed')

#Forest Story line
if location=='Forest':
    Posters_bought = int(input(f'Jeff: Hello {name} my name is Jeff, I am a local, I need help buying flyers for my missing cat, if you’d be so kind I really need some help buying flyers, how many flyers could you buy for me?: '))
    if Posters_bought <= 0:
        print('Jeff: Oh I really thought you’d help me… Well I guess we both better get home, wish my cat could do the same')
        print('GAME OVER: you went home unlike Jeffs cat... you should of help')
    if (Posters_bought > 0) and (Posters_bought < 25):
        print('Jeff: thanks for the help but sadly I don’t think that going to be enough, guess we both better head home.')
        print('GAME OVER: You went home unlike Jeffs cat... you could have printed more poster you know')
    if Posters_bought >= 25:
        treasure = input('Jeff: thank you so much for your help this will definitely help find my cat! As a reward you can have either gold, rubies, or a free ride home?: ')
        if treasure=='gold' or treasure=='rubies':
            print('Jeff: Great choice! You’ll be rich! Time to start the walk home with full pockets.')
            print('GAME OVER: you went home rich and Jeff found his cat')
        elif treasure=='a free ride home':
            print(f'Jeff: No place like home! Wise choice, hopefully we meet again soon {name}')
            print('GAME OVER: you got home safe and Jeff found his cat with your help')

