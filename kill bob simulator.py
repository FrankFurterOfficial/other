#import modules
import random as r
#setup bob
bob_attacks = {'punch' : 3, #attack : damage
                'kick' : 4,
                'dropkick' : 5,
                'fireball' : 7,
                'chainsaw' : 9}
bob_actions = {'defend' : 1, #defense increase (-x damage)
                'cower' : 2, #defense increase (-x damage)
                'hide' : 25} #x% chance to miss
bob_action_names = ['defend','cower','hide']
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
                'hide' : 15, #x% chance for sire bob's attack to miss
                'charge' : 3} #gain 3 points
player_health = 100
player_points = 15
player_defense = 0

while bob_health > 0:
    current_paction = input('action?\nattack, action\n')

    if current_paction == 'attack':

        while current_paction == 'attack':
            player_attack = int(input(f'Which attack(number)?\nATTACK\t\tDAMAGE\tCOST\npunch\t\t{player_attacks['punch']}\t{player_attack_cost[0]}\nkick\t\t{player_attacks['kick']}\t{player_attack_cost[1]}\nverbal abuse\t{player_attacks['verbal abuse']}\t{player_attack_cost[2]}\nfireball\t{player_attacks['fireball']}\t{player_attack_cost[3]}\npaper ball\t{player_attacks['Paperball']}\t{player_attack_cost[4]}\n'))
            if player_points > player_attack_cost[player_attack-1]-1:
                player_points -= player_attack_cost[player_attack-1]
                bob_health -= player_attacks[player_attack_names[player_attack-1]]
                print(f'Points Left: {player_points}')
                print(f'you used {player_attack_names[player_attack-1]}')
                input(f'bob took {player_attacks[player_attack_names[player_attack-1]]} damage, {bob_health} reamining\n')
                current_paction = 'none'
            else:
                input(f'not enough points dingus\n')
        while current_paction == 'none':
            input('Bob is choosing (press enter)\n')
            #set up bob "ai" (attack less defend more if lower health and vice versa)
            if bob_health == 100:
                bob_decision = r.randint(0,1)
            #75-99 health
            elif bob_health < 100 and bob_health >74:
                bob_rand = r.randint(1,100)
                if bob_rand > 79:
                    bob_decision = r.randint(0,2)
                    bob_action_type = 'action'
                    print(bob_decision)
                else:
                    bob_decision = r.randint(0,1)
                    bob_action_type = 'attack'
                    print(bob_decision)
            #50-75 health
            elif bob_health < 76 and bob_health > 49:
                bob_rand = r.randint(1,100)
                if bob_rand > 54:
                    bob_decision = r.randint(0,2)
                    bob_action_type = 'action'
                    print(bob_decision)
                else:
                    bob_decision = r.randint(0,3)
                    bob_action_type = 'attack'
                    print(bob_decision)
            #25-50 health
            elif bob_health < 24 and bob_health > 49:
                bob_rand = r.randint(1,100)
                if bob_rand > 49:
                    bob_decision = r.randint(0,2)
                    bob_action_type = 'action'
                    print(bob_decision)
                else:
                    bob_decision = r.randint(0,4)
                    bob_action_type = 'attack'
                    print(bob_decision)
            #1-25 health
            elif bob_health < 0 and bob_health > 24:
                bob_rand = r.randint(1,100)
                if bob_rand > 39:
                    bob_decision = (0,2)
                    bob_action_type = 'action'
                    print(bob_decision)
                else:
                    bob_decision = r.randint(0,3)
                    bob_action_type = 'attack'
                    print(bob_decision)
            print(f'bob used {bob_action_type}: {bob_attack_names[bob_decision]}')
            if bob_action_type == 'attack':
                player_health -= bob_attacks[bob_attack_names[bob_decision]] - player_defense
                print(f'you take {bob_attacks[bob_attack_names[bob_decision]] - player_defense} damage, {player_health} remaining')