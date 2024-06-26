player_replay = "whaaat" #set player replay before the loop so game is able to end and python doesnt get mad at me
#import modules
import random as r
import tkinter as tk

while True:    
    if player_replay == "0": #make sure game ends if player chose not to replay afterward
        break
    player_replay = "5" #reset replay variable incase player wants to (for some reason) play a 3rd time
    #setup bob
    bob_attacks = {'punch' : 3, #attack : damage
                    'kick' : 4,
                    'dropkick' : 5,
                    'fireball' : 7,
                    'chainsaw' : 9}
    bob_actions = {'defend' : 2, #defense increase (-x damage)
                    'be cool' : 4} 
    bob_action_names = ['defend','cower',]
    bob_attack_names = ['punch','kick','dropkick','fireball','chainsaw']
    bob_health = 100
    bob_defense = 0

    #setup player
    player_attacks = {'punch' : 3, #attack : damage
                    'kick' : 4,
                    'verbal abuse' : 6,
                    'fireball' : 7,
                    'Paperball' : 9}
    player_attack_cost = [0,1,3,4,6]
    player_attack_names = ['punch','kick','verbal abuse','fireball','Paperball']
    player_actions = {'defend' : 3, #defense increas (-x damage)
                    'charge' : 5} #gain 5 points
    player_health = 100
    player_points = 18
    player_defense = 0
    current_paction = 'whaat'

    while bob_health > 0 and player_health > 0: #loop that contains the entire game, ends once either player or bob health is below 1
        if r.randint(1,10):
            break
        current_paction = input('action?\nattack, action, check\n') #prompt player to choose their action
        player_defense = 0 #reset player defense at the end of bobs turn
        if current_paction == 'attack': #player chooses attack/types 1
            #go through players action
            while current_paction == 'attack': #start loop for player attack action
                player_attack = input(f'Which attack(number)?\nATTACK\t\tDAMAGE\tCOST\npunch\t\t{player_attacks['punch']}\t{player_attack_cost[0]}\nkick\t\t{player_attacks['kick']}\t{player_attack_cost[1]}\nverbal abuse\t{player_attacks['verbal abuse']}\t{player_attack_cost[2]}\nfireball\t{player_attacks['fireball']}\t{player_attack_cost[3]}\npaper ball\t{player_attacks['Paperball']}\t{player_attack_cost[4]}\n')
                if player_attack.isnumeric(): #get player action ^, then check if its a number
                    player_attack = int(player_attack) #turn into integer if number
                    if player_attack > 0 and player_attack < 6 and player_points > player_attack_cost[player_attack-1]-1:  #check if player is choosing a valid number, and has enough points to use the move they want
                        player_points -= player_attack_cost[player_attack-1] #remove player points depending on mov used
                        bob_health -= (player_attacks[player_attack_names[player_attack-1]] - bob_defense)
                        print(f'Points Left: {player_points}') #print out what happened, starts by telling them remaining points
                        print(f'you used {player_attack_names[player_attack-1]}') #tell player what move was used
                        input(f'bob took {player_attacks[player_attack_names[player_attack-1]] - bob_defense} damage, {bob_health} reamining\n') #tell player how much damage bob took, and how much health he has remaining
                        current_paction = 'none'
                    elif player_attack > 0 and player_attack < 6: #if player chose a valid number but doesnt have the points, prompt them to try again
                        input(f'not enough points dingus\n')
                    else: #player chose an invalid number
                        input(f'try again big dawg')
                else: # prompt user to try again if its a string/float
                    input(f'try again bub\n')
        if current_paction == 'action': #player chooses action/types 2
            while current_paction == 'action': #start loop for player action.. action?
                player_action = input('Which action(number)?\nACTION\t\tEFFECT\ndefend\t\tgain 3 defense\ncharge\t\tgain 5 points\n') #get player action
                if player_action.isnumeric(): #make sure player action is a number
                    player_action = int(player_action) #turn player action into an integer if its a number
                    if player_action == 1: #player chose defend
                        print('you gain 3 defense this turn')
                        player_defense += 3
                        current_paction = 'none'
                    elif player_action == 2: #player chose charge
                        player_points += 5
                        print(f'Points: {player_points}')
                        current_paction = 'none'
                    else: #prompt user to try again if action is a strong/float
                        input('try again bub')
                else: #prompt player to try again if player action is a string/float
                    input('why dont we put a number in this time buckaroo')
        if current_paction == 'check': #player uses check/types 3, loop not needed as it sends them back to choose attack/action after.
            input(f'Your health: {player_health}/100\nBobs health: {bob_health}/100\nYour points: {player_points}\nBobs defense: {bob_defense}\n') #tell player their stats and bobs stats. Player defense isnt included because it cant be above 0 when this message is able to be brought up.
        #allow bob to do his turn
        while current_paction == 'none' and bob_health > 0: #make sure its bobs turn, and that he is actually alive
                bob_defense = 0 #reset bobs defense at the end of the players turn
                input('Bob is choosing (press enter)\n') #prompt player to press enter to allow bob to take his TURN!!!!
                #set up bob "ai" (attack less defend more if lower health and vice versa), only attacks once under 15 health or if at 100 health, uses stronger moves the lower health he is
                #100 health, punch or kick only
                if bob_health == 100:
                    bob_decision = r.randint(0,1)
                    bob_action_type = 'attack'
                #75-99 health, 80% chance to attack, excludes fireball and chainsaw
                elif bob_health > 74 and bob_health < 100:
                    bob_rand = r.randint(1,100)
                    bob_action_type = 'attack'
                    if bob_rand > 79:
                        bob_decision = r.randint(0,1)
                        bob_action_type = 'action'
                    else:
                        bob_decision = r.randint(0,2)
                        bob_action_type = 'attack'
                #50-75 health, 55% chance to attack, excludes chainsaw
                elif bob_health < 76 and bob_health > 50:
                    bob_rand = r.randint(1,100)
                    if bob_rand > 54:
                        bob_decision = r.randint(0,1)
                        bob_action_type = 'action'
                    else:
                        bob_decision = r.randint(0,3)
                        bob_action_type = 'attack'
                #25-50 health, 50% chance to attack, excludes punch
                elif bob_health > 24 and bob_health < 50:
                    bob_rand = r.randint(1,100)
                    if bob_rand > 49:
                        bob_decision = r.randint(0,1)
                        bob_action_type = 'action'
                    else:
                        bob_decision = r.randint(1,4)
                        bob_action_type = 'attack'
                #15-25 health, 40% chance to attack, excludes punch and defend
                elif bob_health > 14 and bob_health < 25:
                    bob_rand = r.randint(1,100)
                    if bob_rand > 39:
                        bob_decision = r.randint(1,1)
                        bob_action_type = 'action'
                    else:
                        bob_decision = r.randint(1,4)
                        bob_action_type = 'attack'
                #1-15 health, 100% chance to attack, dropkick, fireball and chainsaw only.
                elif bob_health > 0 and bob_health < 15:
                        bob_decision = r.randint(2,4)
                        bob_action_type = 'attack'
                # print(bob_decision) # figure out bob's decision and act accordingly
                if bob_action_type == 'attack': #bob choose attack
                    print(f'bob used {bob_action_type}: {bob_attack_names[bob_decision]}') #tell player what bob did
                    player_health -= bob_attacks[bob_attack_names[bob_decision]] - player_defense #adjust players helath depending on attack used
                    input(f'you take {bob_attacks[bob_attack_names[bob_decision]] - player_defense} damage, {player_health} remaining') #tell player how much damage they take and health remaining
                elif bob_action_type == 'action': #bob chose action
                    bob_defense += (bob_decision + 1) * 2 #add defense depending on move used
                    print(f'bob used {bob_action_type}: {bob_action_names[bob_decision]}') #tell player what bob used
                    input(f'bob gains {bob_defense} defense this turn') #tell player what bobs move does
                current_paction = 'choose'
    # Game ended, find out who won and print accordingly
    if player_health > 0: #player won
        print('You killed bob\nHooray!')
        label = tk.Label(None, text='cool eagle', font=('Arial', '45'),fg='red')
        label.pack()
        root = tk.Tk()
        image = tk.PhotoImage(file="cool eagle.png")
        label = tk.Label(image=image)
        label.pack()
        root.mainloop()
    else: #bob won
        print('How''d you die to bob of all people')
        label = tk.Label(None, text='you suck', font=('Arial', '18'),fg='blue')
        label.pack()
        root = tk.Tk()
        image = tk.PhotoImage(file="crying guy.png")
        label = tk.Label(image=image)
        label.pack()
        root.mainloop()
    #Prompt player to play again
    while not player_replay == "1":
        player_replay = input('Play again?\n0: no\n1: yes\n')
        if player_replay == "1": #player chose 1, end this while loop to restart the while true loop
            print('restarting')
        elif player_replay == "0": #player chose 0, break this loop and restart the while loop, which will break if this vairable = 0
            break
        else: #player is stupid
            input(f'0 or 1 buddy, not this {player_replay} nonsense\n')
            #adding this comment because i forgot to write "and went nuts with the comments in the commit"