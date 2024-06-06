#import modules
import random as r
#setup bob
bob_attacks = {'punch' : 3, #attack : damage
                'kick' : 4,
                'dropkick' : 5,
                'fireball' : 7,
                'chainsaw' : 9}
bob_actions = {'defend' : 1, #defense increase (-x damage)
                'be cool' : 2} 
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
player_actions = {'defend' : 1, #defense increas (-x damage)
                'charge' : 3} #gain 3 points
player_health = 100
player_points = 15
player_defense = 0
current_paction = 'whaat'

while bob_health > 0:
    print(current_paction)
    current_paction = input('action?\nattack, action\n')
    player_defense = 0
    if current_paction == 'attack':
        #go through players action
        while current_paction == 'attack':
            player_attack = int(input(f'Which attack(number)?\nATTACK\t\tDAMAGE\tCOST\npunch\t\t{player_attacks['punch']}\t{player_attack_cost[0]}\nkick\t\t{player_attacks['kick']}\t{player_attack_cost[1]}\nverbal abuse\t{player_attacks['verbal abuse']}\t{player_attack_cost[2]}\nfireball\t{player_attacks['fireball']}\t{player_attack_cost[3]}\npaper ball\t{player_attacks['Paperball']}\t{player_attack_cost[4]}\n'))
            if player_points > player_attack_cost[player_attack-1]-1 and player_attack > 0 and player_attack < 6:
                player_points -= player_attack_cost[player_attack-1]
                bob_health -= player_attacks[player_attack_names[player_attack-1]] - bob_defense
                print(f'Points Left: {player_points}')
                print(f'you used {player_attack_names[player_attack-1]}')
                input(f'bob took {player_attacks[player_attack_names[player_attack-1]]} damage, {bob_health} reamining\n')
                current_paction = 'none'
            else:
                if player_attack > 0 and player_attack < 6:
                    input(f'not enough points dingus\n')
                else:
                    input(f'try again bub\n')
    if current_paction == 'action':
        while current_paction == 'action':
            player_action = int(input('Which action(number)?\nACTION\t\tEFFECT\ndefend\t\tgain 1 defense\ncharge\t\tgain 3 points\n'))
            if player_action == 1:
                player_defense += 1
                current_paction = 'none'
            elif player_action == 2:
                player_points += 3
                current_paction = 'none'
            else:
                input('try again bub')
            
    #allow bob to do his turn
    while current_paction == 'none':
            bob_defense = 0
            input('Bob is choosing (press enter)\n')
            #set up bob "ai" (attack less defend more if lower health and vice versa), only attacks once under 15 health
            if bob_health == 100:
                bob_decision = r.randint(0,1)
                bob_action_type = 'attack'
            #75-99 health
            elif bob_health > 74 and bob_health < 100:
                bob_rand = r.randint(1,100)
                bob_action_type = 'attack'
                if bob_rand > 79:
                    bob_decision = r.randint(0,1)
                    bob_action_type = 'action'
                    print(bob_decision)
                else:
                    bob_decision = r.randint(0,1)
                    bob_action_type = 'attack'
                    print(bob_decision)
            #50-75 health
            elif bob_health < 76 and bob_health > 50:
                bob_rand = r.randint(1,100)
                if bob_rand > 54:
                    bob_decision = r.randint(0,1)
                    bob_action_type = 'action'
                    print(bob_decision)
                else:
                    bob_decision = r.randint(0,3)
                    bob_action_type = 'attack'
                    print(bob_decision)
            #25-50 health
            elif bob_health > 24 and bob_health < 50:
                bob_rand = r.randint(1,100)
                if bob_rand > 49:
                    bob_decision = r.randint(0,1)
                    bob_action_type = 'action'
                    print(bob_decision)
                else:
                    bob_decision = r.randint(0,4)
                    bob_action_type = 'attack'
                    print(bob_decision)
            #15-25 health
            elif bob_health > 14 and bob_health < 25:
                bob_rand = r.randint(1,100)
                if bob_rand > 39:
                    bob_decision = (0,1)
                    bob_action_type = 'action'
                    print(bob_decision)
                else:
                    bob_decision = r.randint(0,4)
                    bob_action_type = 'attack'
                    print(bob_decision)
            #1-15 health
            elif bob_health > 0 and bob_health < 15:
                    bob_decision = r.randint(0,4)
                    bob_action_type = 'attack'
                    print(bob_decision)
            if bob_action_type == 'attack':
                print(f'bob used {bob_action_type}: {bob_attack_names[bob_decision]}')
                player_health -= bob_attacks[bob_attack_names[bob_decision]] - player_defense
                input(f'you take {bob_attacks[bob_attack_names[bob_decision]] - player_defense} damage, {player_health} remaining')
            elif bob_action_type == 'action':
                print(f'bob used {bob_action_type}: {bob_attack_names[bob_decision]}')
                bob_defense += bob_decision + 1
                print(f'bob used {bob_action_type}: {bob_action_names[bob_decision]}')
                input(f'bob gains {bob_defense} defense')
            current_paction = 'choose'