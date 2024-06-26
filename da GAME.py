print('\nsubscibe to dudetocartman\n')
#hi guys
#Import modules
import random as r
import os
import tkinter as tk
#open title screen window
root = tk.Tk()
label = tk.Label(None, text='Close this window to play', font=('Arial', '45'),fg='black')
label.pack()
image = tk.PhotoImage(file="image.png")
label = tk.Label(image=image)
label.pack()
root.mainloop()
#create blank lists for the types of moves
atk_list = []
debuff_list = []
buff_list = []
move_list = []
#setup classes
class stats():
    def __init__(self,Hp: int, Atk: int,Def: int,Spd: int):
        #set current stats
        self.Hp = Hp
        self.Atk = Atk
        self.Def = Def
        self.Spd = Spd
        #set max/base stats
        self.MHp = Hp
        self.BAtk = Atk
        self.BDef = Def
        self.BSpd = Spd
    def __str__(self): #print stats
        return f'Hp: {self.Hp}/{str(self.MHp):12}Atk: {self.Atk}\nDef: {str(self.Def):15}Spd: {self.Spd}'
    def __gt__(self, other): #compare speed
        if self.Spd > other.Spd:
            return self
        elif other.Spd > self.Spd:
            return other
        else:
            return None
        

class Creature(): #Create creature class
    def __init__(self, name, type, stats):
        self.name = name
        self.type = type
        self.base_stats = stats
        self.cur_stats = stats
    def getmoves(self,movelist): #Assign moves
        self.moves = movelist

class moves(): #Create moves class
    def __init__(self,input_name = '', input_description = '', input_effect_number = 0, input_type = ''):
        self.name = input_name
        self.description = input_description
        self.effect_number = input_effect_number
        self.type = input_type
    def __str__(self): #Ovveride print function to print move name
        print(self.name)

    #function to use a move
    def use(self,user : Creature,opponent : Creature):
        if self.type == 'Atk':#checking if the attack type is an attack
            # print(user.cur_stats.Atk)
            damage = user.cur_stats.Atk + self.effect_number - opponent.cur_stats.Def
            if damage < 0:
                    damage = 1
            else: 
                opponent.cur_stats.Hp -= damage
                if user.cur_stats.Hp < 0: #Make sure player hp doesnt go below 0
                    user.cur_stats.Hp = 0
            print(f'{user.name} attacked {opponent.name} with {self.name}\n{opponent.name} takes {damage} damage, leaving them with {opponent.cur_stats.Hp}/{opponent.cur_stats.MHp} Hp left.')
        if 'De' in self.type:#checking if the attack type is a debuff
            if self.type == "DeAtk":
                opponent.cur_stats.Atk -= self.effect_number
                print(f'{user.name} used {self.name} on {opponent.name}!\n{opponent.name}s attack is now {opponent.cur_stats.Atk}')
            elif self.type == "DeDef":
                opponent.cur_stats.Def -= self.effect_number
                print(f'{user.name} used {self.name} on {opponent.name}!\n{opponent.name}s defense is now {opponent.cur_stats.Def}')
            elif self.type == "DeSpd":
                opponent.cur_stats.Spd -= self.effect_number
                print(f'{user.name} used {self.name} on {opponent.name}!\n{opponent.name}s speed is now {opponent.cur_stats.Spd}')

        if 'Bu' in self.type: #checking if the attack type is a buff
            if self.type == "BuAtk": #Buff Attack
                user.cur_stats.Atk += self.effect_number
                print(f'{user.name} used {self.name} on themselves!\n{user.name}s attack is now {user.cur_stats.Atk}')
            elif self.type == "BuDef": #Buff Defense
                user.cur_stats.Def += self.effect_number
                print(f'{user.name} used {self.name} on themselves!\n{user.name}s defense is now {user.cur_stats.Def}')
            elif self.type == "BuSpd": #Buff Speed
                user.cur_stats.Spd += self.effect_number
                print(f'{user.name} used {self.name} on themselves!\n{user.name}s speed is now {user.cur_stats.Spd}')
            elif self.type == "BuHp": #Buff HP (heal)
                user.cur_stats.Hp += self.effect_number
                if user.cur_stats.Hp > user.cur_stats.MHp: #Make sure player hp doesnt go over max
                    user.cur_stats.Hp = user.cur_stats.MHp
                print(f'{user.name} used {self.name} on themselves!\n{user.name}s Hp is now {user.cur_stats.Hp}/{user.cur_stats.MHp}')
        input('Press enter to continue')

def AssignStats(HpR,DefR,SpdR,AtkR): #Function to randomly assign stats based on a value
    if HpR == 0:
        Hp = r.randint(70,90)
    elif HpR == 1:
        Hp = r.randint(85,115)
    elif HpR == 5:
        Hp = r.randint(120,180)
    else:
        Hp = r.randint(115,160)

    if DefR == 0:
        Def = r.randint(1,5)
    elif DefR == 1:
        Def = r.randint(4,9)
    else:
        Def = r.randint(8,12)

    if SpdR == 0:
        Spd = r.randint(1,5)
    elif SpdR == 1:
        Spd = r.randint(4,9)
    else:
        Spd = r.randint(8,12)

    if AtkR == 0:
        Atk = r.randint(1,5)
    elif AtkR == 1:
        Atk = r.randint(4,9)
    elif AtkR == 700:
        Atk = r.randint(999,999)
    else:
        Atk = r.randint(8,12)

    return stats(Hp,Def,Spd,Atk)

def clear(): #Function to clear the screen
        os.system('cls')

def GenerateMove(name,desc,effect,type): #Function to generate move data
    return moves(name,desc,effect,type)    


#Assign creature classes to lists based on their class and assign their stats
GlassCannon = [Creature('Lebron James', 'GlassCannon',AssignStats(0,0,2,2)), Creature('Kevin Huerter', 'GlassCannon',AssignStats(0,0,2,2))]
Ranger = [Creature('Jose Alvarado', 'Ranger',AssignStats(1,0,1,2)), Creature('Barack Obama', 'Ranger',AssignStats(1,0,1,2))]
Aggresive = [Creature('Hellen Keller', 'Aggresive',AssignStats(2,2,2,2)), Creature('Kevin Hart', 'Aggresive',AssignStats(2,1,2,0))]
Dunker = [Creature('Stephen Curry', 'Bully',AssignStats(1,1,0,2)), Creature('Michelle Obama', 'Bully',AssignStats(1,1,0,2))]
Average = [Creature('Anthony Davis', 'Average',AssignStats(1,1,1,1)), Creature('Micheal Jordan', 'Average',AssignStats(1,1,1,1))]
Tank = [Creature('Kevin Durant', 'Tank',AssignStats(2,2,0,1)),Creature('Freddy Fazbear', 'Tank',AssignStats(5,2,2,2))]




def turn(player_1 : Creature,player_2 : Creature): #Function for taking a turn
    while player_1.cur_stats.Hp > 0:
        print(f'\n{player_1.name}, Do you want to attack or view stats') #Ask player to either attack or view their stats
        if player_1.cur_stats.Hp > 0:
            player_option = input('1 for attack\n2 for view stats\n') 
            if player_option == '1':
                player_move_choice = input(f'Select a move:\n1 - {player_1.moves[0].name}\n2 - {player_1.moves[1].name}\n3 - {player_1.moves[2].name}\n4 - {player_1.moves[3].name}\nSelection: ')
                if player_move_choice == '1': #Player choose 1st move, use it
                    player_1.moves[0].use(player_1,player_2)
                    break
                elif player_move_choice == '2': #Player choose 2nd move, use it
                    player_1.moves[1].use(player_1,player_2)
                    break
                elif player_move_choice == '3': #Player choose 3rd move, use it
                    player_1.moves[2].use(player_1,player_2)
                    break
                elif player_move_choice == '4': #Player choose 4th move, use it
                    player_1.moves[3].use(player_1,player_2)
                    break
                else: #Player did not enter a number 1-4
                    print('Please enter 1-4')
                    input()

            elif player_option == '2': #Player chose to view stats
                print(f'{player_1.name} stats:')
                print(f'{player_1.cur_stats}\n')
                print('Attacks:\nName\t\tEffect\tDescription') #Display stats
                print(f'{player_1.moves[0].name:12}\t{player_1.moves[0].effect_number}\t{player_1.moves[0].description}')
                print(f'{player_1.moves[1].name:12}\t{player_1.moves[1].effect_number}\t{player_1.moves[1].description}')
                print(f'{player_1.moves[2].name:12}\t{player_1.moves[2].effect_number}\t{player_1.moves[2].description}')
                print(f'{player_1.moves[3].name:12}\t{player_1.moves[3].effect_number}\t{player_1.moves[3].description}')
                input()
                continue #Restart loop

def round (Player1_fellow, Player2_fellow): #Function to take a round
    if Player1_fellow.cur_stats.Spd > Player2_fellow.cur_stats.Spd: #If player 1 has higher speed, they go first
        turn(Player1_fellow, Player2_fellow)
        turn(Player2_fellow, Player1_fellow)
    elif Player1_fellow.cur_stats.Spd < Player2_fellow.cur_stats.Spd: #If player 2 has higher speed, they go first
        turn(Player2_fellow, Player1_fellow)
        turn(Player1_fellow, Player2_fellow)
    else: #If both players have equal speed, a random player is chosen
        num3 = r.randint(1,2)
        print('Both players have equal speed, choosing random player')
        print(f'Player chosen: Player {num3}')
        if num3 == 1:
            turn(Player1_fellow, Player2_fellow)
            turn(Player2_fellow, Player1_fellow)
        if num3 == 2:
            turn(Player2_fellow, Player1_fellow)
            turn(Player1_fellow, Player2_fellow)
playagain = 0


#main program
while True: #Keep game in a loop
    Player1_Guy = 1 #reset player 1
    Player2_Guy = 1 #reset player 2
    if playagain == 'naw': #If player choose not to replay, end the loop/game
        break
    playagain = 1 #reset play again vairable
    selection = [] #clear selection list then refill it
    selection.append(GlassCannon[r.randint(0,len(GlassCannon)-1)])
    selection.append(Ranger[r.randint(0,len(Ranger)-1)])
    selection.append(Aggresive[r.randint(0,len(Aggresive)-1)])
    selection.append(Dunker[r.randint(0,len(Dunker)-1)])
    selection.append(Average[r.randint(0,len(Average)-1)])
    selection.append(Tank[r.randint(0,len(Tank)-1)])
    #Create the moves and put them in the appropiate lists
    atk_list = []
    debuff_list = []
    buff_list = []
    atk_list.append(GenerateMove('Dunk','Dunk on em', 8, 'Atk'))
    atk_list.append(GenerateMove('Slam Dunk','Slam dunk on em', 13, 'Atk'))
    atk_list.append(GenerateMove('3 pointer','shoot a crazy 3 pointer', 11, 'Atk'))
    atk_list.append(GenerateMove('free throw','take a cheat shot, cheater', 10, 'Atk'))
    atk_list.append(GenerateMove('halfcourt','go CRAZY', 18, 'Atk'))
    atk_list.append(GenerateMove('layup','go make a layup I guess. Lame.', 13, 'Atk'))
    atk_list.append(GenerateMove('bank shot','I dont know what a bank shot is', 16, 'Atk'))
    atk_list.append(GenerateMove('hook shot','go wild with da hook shot', 14, 'Atk'))
    atk_list.append(GenerateMove('fireball','Cast fireball. This isnt even a basketball move', 23, 'Atk'))
    debuff_list.append(GenerateMove('Ankle breaker','break those ankles, decreasing speed', 3, 'DeSpd'))
    debuff_list.append(GenerateMove('fake-out','fake them out, decreasing attack', 2, 'DeAtk'))
    debuff_list.append(GenerateMove('block','block their shot, decreasing their defense', 1, 'DeDef'))
    buff_list.append(GenerateMove('dribble','Stall to dribble, healing you', 21, 'BuHp'))
    buff_list.append(GenerateMove('pass','Pass the ball to your teammate, making you lighter and buffing your speed', 5, 'BuSpd'))
    buff_list.append(GenerateMove('alley oop','do whatever an alley oop is, gain attack somehow', 4, 'BuAtk'))
    buff_list.append(GenerateMove('Pivot','Kick your opponent in the head, gaining defense', 2, 'BuDef'))
    #Blank out the player move lists
    player1_hold = []
    player2_hold = []

    #Assign player 1's moves
    num = r.randint(0,len(atk_list) - 1) #Attack 1
    player1_hold.append(atk_list[num])
    atk_list.pop(num)
    num = r.randint(0,len(atk_list) - 1) #Attack 2
    player1_hold.append(atk_list[num])
    atk_list.pop(num)
    num = r.randint(0,len(buff_list) - 1) #Buff move
    player1_hold.append(buff_list[num])
    buff_list.pop(num)
    num = r.randint(0,len(debuff_list) - 1) #DeBuff move
    player1_hold.append(debuff_list[num])
    debuff_list.pop(num)

    #Assign player 2's moves
    num = r.randint(0,len(atk_list) - 1) #Attack 1
    player2_hold.append(atk_list[num])
    atk_list.pop(num)
    num = r.randint(0,len(atk_list) - 1) #Attack 2
    player2_hold.append(atk_list[num])
    atk_list.pop(num)
    num = r.randint(0,len(buff_list) - 1) #Buff move
    player2_hold.append(buff_list[num])
    buff_list.pop(num)
    num = r.randint(0,len(debuff_list) - 1) #DeBuff move
    player2_hold.append(debuff_list[num])
    debuff_list.pop(num)
    # print(player1_hold)
    # print(player2_hold)

    while 1 == 1: #Ask player 1 to select their character
        Player1_Guy = input(f'Select your player (Player 1): \n1 - {selection[0].name}\t Glass Cannon\n2 - {selection[1].name}\t Ranger\n3 - {selection[2].name:20} Aggresive\n4 - {selection[3].name}\t Bully\n5 - {selection[4].name}\t Average\n6 - {selection[5].name}\t Tank\nSelection: ')
        if Player1_Guy.isnumeric(): #Check if input was a number and convert to integer if it was
            Player1_Guy = int(Player1_Guy)
            if Player1_Guy > 0 and Player1_Guy < 7:
                print(f'Player 1 chose {selection[Player1_Guy - 1].name}\n') 
                num2 = Player1_Guy
                Player1_Guy = selection[Player1_Guy - 1] #Set player 1 to character they chose
                selection.pop(num2 - 1) #Remove player 1's character from the list
                break
            else: #Input was a number but not in the range
                print('Please choose a number in the range')
        else: #Input wasnt a number
            print('please insert a number')
    while 1 == 1:
        num = 0
        print('Select your player (Player2):') #Ask player 2 to select their character
        for i in selection:
            num += 1
            print(f'{num} - {i.name:20}{i.type}')
        Player2_Guy = input('Selection: ')
        if Player2_Guy.isnumeric(): #Check if input was a number and convert to integer if it was
            Player2_Guy = int(Player2_Guy)
            if Player2_Guy > 0 and Player2_Guy < 6:
                print(f'Player 2 chose {selection[Player2_Guy - 1].name}')
                Player2_Guy = selection[Player2_Guy - 1] #set player 2 to character they chose
                break #End loop and begin game
            else: #input was a number but not in range
                print('Please choose a number in the range')
        else: #input was not a number
            print('please insert a number')
    # print(player1_hold)
    # print(player2_hold)
    Player1_Guy.getmoves(player1_hold) #assign player 1's moves
    Player2_Guy.getmoves(player2_hold) #assign player 2's moves
    #put somewhere in the main game loop
    
    #shows both player's stats and info
    Player1_Guy.cur_stats.Hp = Player1_Guy.cur_stats.MHp #make sure players health is full before game starts
    Player2_Guy.cur_stats.Hp = Player2_Guy.cur_stats.MHp

    while Player1_Guy.cur_stats.Hp > 0 and Player2_Guy.cur_stats.Hp > 0: #Loop to keep game going aslong as both players have over 0 health
        clear()
        round(Player1_Guy,Player2_Guy)
    if Player1_Guy.cur_stats.Hp > 0: #player 1 wins
        clear()
        input(f'{Player1_Guy.name} has won against {Player2_Guy.name}\n')
    if Player2_Guy.cur_stats.Hp > 0: #player 2 wins
        clear()
        input(f'{Player2_Guy.name} has won against {Player1_Guy.name}\n')
    
    while True: #Loop to ask player if they would like to replay
        playagain = input('Do you want to play again?\n0 - No\n1 - Yes\nSelection: ')
        if playagain.isnumeric(): #Check that their input was a number and convert to integer if it was
            playagain = int(playagain)
            if playagain == 1: #Player chose to play again, clear the console and break this loop, restarting the game
                clear()
                break
            elif playagain == 0: #Player choose to not replay, break loop and set playagain vairable so the main loop breaks, ending the game
                playagain = 'naw'
                break
            else: #Input was not 0 or 1
                input('Please input 0 or 1\n')
        else: #Input was not a number
            input('Invalid input, Please input a number')
