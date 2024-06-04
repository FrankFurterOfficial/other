#setup bob
bob_attacks = {'punch' : 3, #attack : damage
                'kick' : 4,
                'dropkick' : 5,
                'fireball' : 7,
                'chainsaw' : 9}
bob_actions = {'defend' : 1, #defense increase (-x damage)
                'cower' : 2, #defense increase (-x damage)
                'hide' : 25} #x% chance to miss
bob_health = 100

#setup player
player_attacks = {'punch' : 3, #attack : damage
                'kick' : 4,
                'verbal abuse' : 6,
                'fireball' : 7,
                'Paperball' : 9}
player_attack_cost = [0,1,3,4,6]
player_attack_names = ['punch','kick','verbal abuse','fireball','Paperball']
player_actions = {'defend' : 1, 
                'hide' : 15,
                'charge' : 3} #gain 3 points
player_health = 100
player_points = 15

while bob_health > 0:
    current_paction = input('action?\nattack, action\n')

    if current_paction == 'attack':

        while current_paction == 'attack':
            player_attack = int(input(f'Which attack(number)?\nATTACK\t\tDAMAGE\tCOST\npunch\t\t{player_attacks['punch']}\t{player_attack_cost[0]}\nkick\t\t{player_attacks['kick']}\t{player_attack_cost[1]}\nverbal abuse\t{player_attacks['verbal abuse']}\t{player_attack_cost[2]}\nfireball\t{player_attacks['fireball']}\t{player_attack_cost[3]}\npaper ball\t{player_attacks['Paperball']}\t{player_attack_cost[4]}\n'))
            if player_points > player_attack_cost[player_attack-1]-1:
                player_points -= player_attack_cost[player_attack-1]
                print(f'Points Left: {player_points}')
                input(f'you used {player_attack_names[player_attack-1]}')
            else:
                input(f'not enough points dingus\n')