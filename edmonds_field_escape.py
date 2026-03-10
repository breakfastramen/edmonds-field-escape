# terminal adventure project
import random # set up random number generator
import sys # set up sys for exiting the game
# opening title and scene introduction
print("Welcome to Escape from Edmonds Field!")
print("Trolls are attacking Edmonds Field! Flee to Bearlin to escape the Dark Guy and his friends.")
print("You will make choices and fight enemies along the way. Choose wisely and survive!")
print("Choose your character:")

# character selection and stat assignment
valid_choice = False
while valid_choice == False:
    player = input("1. Randy: the Balanced One; 2. Matt: the DPS; 3. Perron: the Tank. Enter the name of your choice: ")
    if player == "Randy":
        player_health = 100
        player_max_health = 100
        player_attack = 20
        player_defense = 20
        weapon = "sword"
        valid_choice = True
        print("You have chosen Randy, the Balanced One. Your health is 100, your attack is 20, and your defense is 20.")
    elif player == "Matt":
        player_health = 90
        player_max_health = 90
        player_attack = 30
        player_defense = 15
        weapon = "dagger"
        valid_choice = True
        print("You have chosen Matt, the DPS. Your health is 90, your attack is 30, and your defense is 15.")
    elif player == "Perron":
        player_health = 110
        player_max_health = 110
        player_attack = 15
        player_defense = 25
        weapon = "axe"
        valid_choice = True
        print("You have chosen Perron, the Tank. Your health is 110, your attack is 15, and your defense is 25.")
    else:
        print("Invalid choice. Please enter your character's name exactly as it appears in the options.")

# begin narrative choice 1
print(f"{player}, you find yourself in the center of Edmonds Field. The town is burning and trolls roam the streets. What do you do?")
print("1. Try to find that super powerful lady wizard and her obviously deadly bodyguard.")
print("2. Try to find the mayor.")
print("3. Flee to the nearby forest.")
if player == "Randy":
    print("4. Go back to my stepdad's farm.")
valid_choice = False
while valid_choice == False:
    choice_1 = input("Enter the number of your choice: ")
    if choice_1 == "1": # safe narrative choice, proceed to choice 2
        valid_choice = True
        print("You decide to find the super powerful lady wizard and her deadly bodyguard. You navigate the burning streets to find them in the town square.")
        print("The lady wizard and her bodyguard are standing next to a smoking pile of troll corpses. The lady wizard strides up to you and speaks.")
        print(f"'Hello {player}, I am Moira, and my bodyguard is Bland. The Dark Guy wants to kill you, so let's get the frick out of here.'")
        # narrative heal
        player_health = player_health + 25
        if player_health > player_max_health:
            player_health = player_max_health
        print(f"You follow Moira and Bland out of the town and you flee down the road to the river. Your health is {player_health}.")
    elif choice_1 == "2": # fight a troll and proceed
        valid_choice = True
        print("The local mayor is also the innkeeper, so you run to the local inn.")
        print("The inn is aflame! A troll carrying a torch sees you and attacks!")
        # combat block
        # troll stat block
        troll_health = 75
        troll_attack = 30
        troll_defense = 0
        while troll_health > 0 and player_health > 0:
        # do a round of combat
            print("A troll swings at you with its mace!")
            if random.random() < 0.5: # miss
                print("You dodge the troll's attack!")
            else:
                print("The troll strikes you with its mace!")
                player_health = player_health - (troll_attack - player_defense)
                print(f"Your health is now {player_health}!")
            print(f"You strike back at the troll with your {weapon}!")
            if random.random() < 0.20: # miss chance is lower so this game is easily playable
                print("You miss the troll!")
            else:
                print("You hit the troll!")
                troll_health = troll_health - (player_attack - troll_defense)
                print(f"The troll's health is now {troll_health}!")
        # resolve combat
        if player_health <= 0:
            print("You have been slain by the troll. Game over.")
            sys.exit()
        else:
            print("You have slain the troll!")
        # end combat block
        print("The trolls have destroyed the inn and the mayor cannot be found. You are approached by the super powerful lady wizard and her bodyguard.")
        print(f"'Hello {player}, I am Moira, and my bodyguard is Bland. The Dark Guy wants to kill you, so let's get the frick out of here.'")
        # combat heal
        player_health = player_health + 10
        if player_health > player_max_health:
            player_health = player_max_health
        print(f"You follow Moira and Bland out of the town and you flee down the road to the river. You recover a small amount of health. Your health is {player_health}.")
    elif choice_1 == "3": # flee to the forest
        valid_choice = True
        print("You decide to flee to the nearby forest.")
        print("You run into the forest and hide behind a tree. A troll searching the area finds you and attacks!")
        # combat block
        # troll stat block
        troll_health = 75
        troll_attack = 30
        troll_defense = 0
        while troll_health > 0 and player_health > 0:
            # do a round of combat
            print("A troll swings at you with its mace!")
            if random.random() < 0.5: # miss
                print("You dodge the troll's attack!")
            else:
                print("The troll strikes you with its mace!")
                player_health = player_health - (troll_attack - player_defense)
                print(f"Your health is now {player_health}!")
            print(f"You strike back at the troll with your {weapon}!")
            if random.random() < 0.20: # miss chance is lower so this game is easily playable
                print("You miss the troll!")
            else:
                print("You hit the troll!")
                troll_health = troll_health - (player_attack - troll_defense)
                print(f"The troll's health is now {troll_health}!")
        if player_health <= 0:
            print("You have been slain by the troll. Game over.")
            sys.exit()
        else:
            print("You have slain the troll!")
        # end combat block
        print("You are found by the super powerful lady wizard and her bodyguard.")
        print(f"'Hello {player}, I am Moira, and my bodyguard is Bland. The Dark Guy wants to kill you, so let's get the frick out of here.'")
        # combat heal
        player_health = player_health + 10
        if player_health > player_max_health:
            player_health = player_max_health
        print(f"You follow Moira and Bland out of the town and you flee down the road to the river. You recover a small amount of health. Your health is {player_health}.")
    elif choice_1 == "4" and player == "Randy": # hidden Randy option
        valid_choice = True
        print("You decide to run to your stepdad's farm.")
        print("You arrive at the farm and find your stepdad has been injured by a troll. The troll sees you and attacks!")
        # combat block
        # troll stat block
        troll_health = 75
        troll_attack = 30
        troll_defense = 0
        while troll_health > 0 and player_health > 0:
            # do a round of combat
            print("A troll swings at you with its mace!")
            if random.random() < 0.5: # miss
                print("You dodge the troll's attack!")
            else:
                print("The troll strikes you with its mace!")
                player_health = player_health - (troll_attack - player_defense)
                print(f"Your health is now {player_health}!")
            print(f"You strike back at the troll with your {weapon}!")
            if random.random() < 0.20: # miss chance is lower so this game is easily playable
                print("You miss the troll!")
            else:
                print("You hit the troll!")
                troll_health = troll_health - (player_attack - troll_defense)
                print(f"The troll's health is now {troll_health}!")
        if player_health <= 0:
            print("You have been slain by the troll. Game over.")
            sys.exit()
        else:
            print("You have slain the troll!")
        # end combat block
        print("You are found by the super powerful lady wizard and her bodyguard.")
        print("The super powerful lady wizard uses magic to heal your stepdad, then she speaks to you.")
        print(f"'Hello {player}, I am Moira, and my bodyguard is Bland. The Dark Guy wants to kill you, so let's get the frick out of here.'")
        # combat heal
        player_health = player_health + 10
        if player_health > player_max_health:
            player_health = player_max_health
        print(f"You follow Moira and Bland out of the town and you flee down the road to the river. You heal a small amount. Your health is {player_health}.")

    else:
        print("You stand there, confused. (Invalid choice. Please enter a valid option.)")
input("Press Enter to continue...")

# begin narrative choice 2
print("You flee Edmonds Field with Moira and Bland, urging your horses with all speed to the river crossing at Tairen Fairy.")
print("After a harrowing flight with the sounds of howling trolls fading into the distance behind you, you find yourself surrounded by premorning fog in the crossing town of Tairen Fairy.")
print("Bland turns to you and says, 'We must cross the river to buy some time, nerfherder. We aren't safe yet.'")
print("The town still slumbers in the fog. Trolls are not far behind, so you must hurry. What do you do?")
print("1. Go directly to the ferry and try to cross the river.") # risky choice, you run into issues trying to cross and Moira saves you, but you lose some health and proceed to choice 3
print("2. Try to find the ferryman and get him to help you cross.") # safe option, ferryman helps you cross, you get a narrative heal, and you proceed to choice 3
print("3. Hide in the town and wait for the trolls to pass.") # triggers combat with a troll, but if you win you cross the river and proceed to choice 3
if player == "Matt":
    print("4. Try to gather information in a dice game at the local tavern.") # hidden Matt option, no combat but you win a dice game and a smuggler offers to help you cross the river, you get a narrative heal
valid_choice = False
while valid_choice == False:
    choice_2 = input("Enter the number of your choice: ")
    if choice_2 == "1":
        valid_choice = True
        print("You decide to rush to the river directly and attempt the crossing yourselves. Speed is of the essence!")
        print("You arrive at the river and find the ferry docked, but the ferryman is not there. You attempt to cross the river on your own, but the current is too strong and you are swept downstream!")
        print("Moira channels her magic to calm the waters, but you lose some health.")
        # narrative damage
        player_health = player_health - 15
        if player_health <= 0:
           print("You have been swept away by the river and drowned. The Dark Guy wins and severs the world from the tapestry of fate. Game over.")
           sys.exit()
        else:
            print(f"You survive the river crossing, but your health is now {player_health}. You and your companions make it to the other side and continue on your journey.")
    elif choice_2 == "2":
        valid_choice = True
        print("You decide to find the ferryman and use his ferry to cross the river.")
        print("Bland leads you and Moira to a sturdy building near the river and pounds on the door.")
        print("A grouchy grizzled grumpus of a man angrily answers the door and wonders why you have woken him so early.")
        print("Bland says, 'We need to cross the river, and I have much gold.' He hands the ferryman a small leather sack that clinks with an indeterminate number of coins.")
        print("The ferryman ferrets away the pouch of coins without looking at it, which tends to happen in these kinds of stories, even though checking the sum would be prudent.")
        print("The ferryman assists your party in an uneventful crossing and you continue on your journey. Regain 20 health.")
        # narrative heal
        player_health = player_health + 20
        if player_health > player_max_health:
            player_health = player_max_health
        print(f"Your health is now {player_health}.")
    elif choice_2 == "3":
        valid_choice = True
        print("You decide to hide in the town and wait for the trolls to pass.")
        print("You hide in the cellar of a townsperson's house, hoping the trolls will not find you.")
        print("Before long, a troll searching the area finds you and attacks!")
        print("Moira crosses her arms beneath her breasts and says coolly, 'If you are the Chosen One, then you are fated to win.'")
        print("Bland grunts derisively and says, 'Let's see if you remember any of those tricks I showed you, idiot.'")
        # combat block
        # troll stat block
        troll_health = 75
        troll_attack = 30
        troll_defense = 0
        while troll_health > 0 and player_health > 0:
            # do a round of combat
            print("A troll swings at you with its mace!")
            if random.random() < 0.5: # miss
                print("You dodge the troll's attack!")
            else:
                print("The troll strikes you with its mace!")
                player_health = player_health - (troll_attack - player_defense)
                print(f"Your health is now {player_health}!")
            print(f"You strike back at the troll with your {weapon}!")
            if random.random() < 0.20: # miss chance is lower so this game is easily playable
                print("You miss the troll!")
            else:
                print("You hit the troll!")
                troll_health = troll_health - (player_attack - troll_defense)
                print(f"The troll's health is now {troll_health}!")
        if player_health <= 0:
            print("You have been slain by the troll. Game over.")
            sys.exit()
        else:
            print("You have slain the troll!")
        # end combat block
        print(f"Moira and Bland nod to each other, and Moira speaks. 'Now you see that you cannot hide from the Dark Guy. You aren't very smart, {player}. Let's get the frick out of here.'")
        print("You find the ferryman and cross the river safely. You regain a small amount of health and continue on your journey.")
        # combat heal
        player_health = player_health + 10
        if player_health > player_max_health:
            player_health = player_max_health
        print(f"Your health is now {player_health}.")
    elif choice_2 == "4" and player == "Matt":
        valid_choice = True
        print("You decide to try to gather information in a dice game at the local tavern.")
        print("You get a lucky roll and win a big bet against a scruffy-looking fellow. Moira sniffs. Bland grunts.")
        print("The scruffy man grins at you and says, 'I'll be in huge trouble if I go home empty-handed.'")
        print("'Give me back half my wager and I can get you across the river unseen, and I'll keep my mouth shut after.'")
        print("You give the smuggler back some coin and he spirits you across the river in his boat.")
        print("You regain some health and continue on your journey.")
        # narrative heal
        player_health = player_health + 25
        if player_health > player_max_health:
            player_health = player_max_health
        print(f"Your health is now {player_health}.")
    else:
        print("You stand there, confused. (Invalid choice. Please enter a valid option.)")
# end choice 2

input("Press Enter to continue...")

# begin narrative choice 3
print("After crossing the river, you continue your flight to Bearlin. Moira is certain that you have only bought yourself a little time.")
print("'We must cross some wilderness to get to Bearlin,' Bland grunts macho-ly. 'Try not to get us killed, farmboy.'")
print("You have several paths before you. What route do you take to Bearlin?")
print("1. Cut across the mountain ridge. Hiding is difficult but it's the most direct route.") # option will trigger combat with drakkar
print("2. Take the long way around the mountain ridge through the forest at its base.") # option provides cover from drakghar but takes longer, small narrative heal
print("3. Cut through the mountain ridge via the mines.") # troll combat, LOTR reference?
if player == "Perron":
    print("4. Stop and listen to the sounds of nature to guide you.") # follow howls of wolves to Bearlin with no encounters, narrative heal
valid_choice = False
while valid_choice == False:
    choice_3 = input("Enter the number of your choice: ")
    if choice_3 == "1":
        valid_choice = True
        print("You decide to cut across the mountain ridge. Your party hikes across the exposed face of the mountain ridge, unable to hide.")
        print("As you make your way across the ridge, you suddenly hear an eerie keening from the skies above.")
        print("Moira smooths her skirts and calmly exposits, 'That is the sound of a drakkar. It is one of the Dark Guy's minions.'")
        print("At that moment, a man-sized creature swoops from above on giant, batlike wings. It croons at you with an odd song and bares its fangs.")
        print("'Block out its song,' Moira tutorials, 'or it will suck out your life force!'")
        print("'I knew a Saldean farmgirl like that once,' Bland grunts gruffly.")
        print("The drakkar approaches you and attacks!")
        # combat block
        # drakkar stat block
        drakkar_health = 90
        drakkar_attack = 35
        drakkar_defense = 0
        while drakkar_health > 0 and player_health > 0:
            # do a round of combat
            print("The drakkar swipes at you with its claws!")
            if random.random() < 0.5: # miss
                print("You dodge the drakkar's attack!")
            else:
                print("The drakkar strikes you with its claws!")
                player_health = player_health - (drakkar_attack - player_defense)
                print(f"Your health is now {player_health}!")
            print(f"You strike back at the drakkar with your {weapon}!")
            if random.random() < 0.20: # miss chance is lower so this game is easily playable
                print("You miss the drakkar!")
            else:
                print("You hit the drakkar!")
                drakkar_health = drakkar_health - (player_attack - drakkar_defense)
                print(f"The drakkar's health is now {drakkar_health}!")
        if player_health <= 0:
            print("You have been slain by the drakkar. Game over.")
            sys.exit()
        else:
            print("You have slain the drakkar!")
        # end combat block
        print(f"You dispatch the drakkar with your {weapon}. You have earned reputation with Bland. Bland now trusts you to not cut off your own fingers by accident.")
        print("You are able to finish crossing the mountain ridge, and you reach Bearlin before nightfall.")
        print("Bearlin is a simple backwater mountain mining city, but you come from a place where shearing sheep is unironically the event of the year, so you are impressed by its rugged majesty.")
        # combat heal
        player_health = player_health + 10
        if player_health > player_max_health:
            player_health = player_max_health
        print(f"You recover a small amount of health as you finally reach an inn and take a bath. Your health is {player_health}.")
    elif choice_3 == "2":
        valid_choice = True
        print("You decide to take the long way around the mountain ridge through the forest at its base.")
        print("The forest provides cover from any potential threats, but it takes longer to navigate.")
        print("You have to push yourself hard to make it to Bearlin before nightfall, so there is little time to rest.")
        print("You recover a small amount of health.")
        # small narrative heal
        player_health = player_health + 10
        if player_health > player_max_health:
            player_health = player_max_health
        print("Bearlin is a simple backwater mountain mining city, but you come from a place where shearing sheep is unironically the event of the year, so you are impressed by its rugged majesty.")
        print(f"You find an inn and discuss your next move. Your health is {player_health}.")
    elif choice_3 == "3":
        valid_choice = True
        print("You decide that cutting through the mines will be the easiest and most direct route.")
        print("Bland shakes his head grimly and explains, 'Beware the mines, simpleton. They are abandoned for a reason.'")
        print("'Isn't this a little too familiar?' you ask.")
        print("'It was the only way to get a publishing deal in the 80s,' Moira intones.")
        print("As you make your way through the dark mines, you get separated from Moira and Bland.")
        print("You stumble across a lone troll, and the troll attacks!")
        # combat block
        # troll stat block
        troll_health = 75
        troll_attack = 30
        troll_defense = 0
        while troll_health > 0 and player_health > 0:
            # do a round of combat
            print("A troll swings at you with its mace!")
            if random.random() < 0.5: # miss
                print("You dodge the troll's attack!")
            else:
                print("The troll strikes you with its mace!")
                player_health = player_health - (troll_attack - player_defense)
                print(f"Your health is now {player_health}!")
            print(f"You strike back at the troll with your {weapon}!")
            if random.random() < 0.20: # miss chance is lower so this game is easily playable
                print("You miss the troll!")
            else:
                print("You hit the troll!")
                troll_health = troll_health - (player_attack - troll_defense)
                print(f"The troll's health is now {troll_health}!")
        if player_health <= 0:
            print("You have been slain by the troll. Game over.")
            sys.exit()
        else:
            print("You have slain the troll!")
        # end combat block
        print("Moira and Bland find you by the sounds of your battle.")
        print("'There you are, Farm Boy of Destiny,' Moira murmurs calmly. 'Let's get the frick out of here.'")
        print("You make your way out of the mines and reach Bearlin before nightfall.")
        print("Bearlin is a simple backwater mountain mining city, but you come from a place where shearing sheep is unironically the event of the year, so you are impressed by its rugged majesty.")
        # combat heal
        player_health = player_health + 10
        if player_health > player_max_health:
            player_health = player_max_health
        print(f"You recover a small amount of health as you finally reach an inn and take a bath. Your health is {player_health}.")
    elif choice_3 == "4" and player == "Perron":
        valid_choice = True
        print("You stop and gather your bearings, opening your mind to the sounds of nature all around you.")
        print("You feel a strange sense of connection with the sound of distantly howling wolves, and you lead Moira and Bland toward the sound.")
        print("The howls of the wolves lead you on a path through the forest that provides cover from the searching minions of the Dark Guy.")
        print("'If you learn to accept your inner wolf, this skill will be OP,' Moira observes.")
        print("You make surprisingly good time reaching Bearlin and have plenty of time to rest. You recover some health.")
        print("Bearlin is a simple backwater mountain mining city, but you come from a place where shearing sheep is unironically the event of the year, so you are impressed by its rugged majesty.")
        # narrative heal
        player_health = player_health + 20
        if player_health > player_max_health:
            player_health = player_max_health
        print(f"Your health is now {player_health}.")
    else:
        print("You stand there, confused. (Invalid choice. Please enter a valid option.)")
# end choice 3

input("Press Enter to continue...")

# begin choice 4
print("You rest for the night at an inn in Bearlin. You have finally made it to safety!")
print("During the night, you are woken by terrible and disturbing dreams. You realize there is a hooded, shadowy figure in the room with you.")
print(f"You spring to your feet and grab your {weapon}. The dark figure fixes you with a glare colder than the grave and speaks.")
print(f"The figure's voice is like the crumbling of rotten earth in a blighted field. 'Your flight ends here, {player}. You cannot escape the Dark Guy!'")
input("Press Enter to regain bladder control.")
print(f"Moira and Bland burst into the room. '{player}, do not underestimate the Myrghul! They are one of the Dark Guy's best mobs!' Moira chides gently.")
print("The Myrghul snarls at the lady wizard and her bodyguard, and you realize that the hood of its pitch black cloak was hiding a face without a nose.")
print(f"'Is everything going to continue to be a thinly-veiled reference to a certain genre-defining fantasy series?' {player} asks.")
print("'Does it help to know I'm not just a gruff bodyguard to a lady wizard, but also a secret king?' Bland asks.")
print("'It really starts to come into its own in the next book,' Moira explains.")
print("Moira fills you with healing magic!")
# boss battle heal
player_health = player_max_health
print(f"Your health is now {player_health}.")
print("The Myrghul draws a blade blacker than the bottom of a covered well on a moonless night. It's, like, dark and scary.")
print("'Serve the Dark Guy or die!' the Myrghul calls.")
print("The Myrghul attacks with blinding speed!")
input("Press Enter for a... B-B-B-B-BOSS BATTLE!")
# combat block
# myrghul stat block
myrghul_health = 100
myrghul_attack = 40
myrghul_defense = 0
while myrghul_health > 0 and player_health > 0:
    # do a round of combat
    print("The Myrghul swings at you with its black sword!")
    if random.random() < 0.45: # miss chance is lower for the myrghul because boss battle
        print("You dodge the Myrghul's attack!")
    else:
        print("The Myrghul slashes you with its sword!")
        player_health = player_health - (myrghul_attack - player_defense)
        print(f"Your health is now {player_health}!")
    print(f"You strike back at the Myrghul with your {weapon}!")
    if random.random() < 0.20: # miss chance is lower so this game is easily playable
        print("You miss the Myrghul!")
    else:
        print("You hit the Myrghul! Bland is impressed!")
        myrghul_health = myrghul_health - (player_attack - myrghul_defense)
        print(f"The Myrghul's health is now {myrghul_health}!")
if player_health <= 0:
    print("You have been slain by the Myrghul. Bland tries to save you, but you disappear with the Myrghul into the shadows. 'Oops,' Moira says. Game over. The Dark Guy wins again.")
    sys.exit()
else:
    print("You have slain the Myrghul!")
input("Press Enter to continue.")
# end combat block
# series of print statements that give the final scene and end the game
print("You stand over the flailing corpse of the Myrghul, black blood trailing from its wounds. Moira sends a healing pulse of magic through you.")
print("'Clearly the Dark Guy no longer worries about exposing its plans,' Moira sequels. 'To ensure your safety, we must reach the city of the lady wizards, Nott Avalon.'")
print("'You almost fought well enough to not embarrass me,' Bland admits. You attempt to resist the urge to mentally label him as New Dad. You fail.")
print("CONGRATULATIONS, PLAYER! You have successfully escaped Edmonds Field and evaded the forces of the Dark Guy.")
print("Stay tuned for the next installment, The Suspciously Shaped Island of Nott Avalon!")
sys.exit()