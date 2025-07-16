import colorama
from colorama import Fore
from art import *
from os import name, system
from random import choice, randint
from time import sleep
import platform
from simple_term_menu import TerminalMenu

class Player():
    '''Player Class for inidividual human players'''
    def __init__(self, name = "undefined", health = 120,
     body_type = "undefined", weapon = "undefined", age = 0):
        self.__name = name
        self.__health = health
        self.__age = age
        self.__body_type = body_type
        self.__weapon = weapon

    def get_name(self):
        '''Gets player name'''
        return self.__name

    def get_health(self):
        '''Gets player health'''
        return self.__health

    def get_body_type(self):
        '''Gets player body type'''
        return self.__body_type

    def get_weapon(self):
        '''Gets player weapon type'''
        return self.__weapon    

    def set_name(self, name):
        '''Sets player name'''
        self.__name = name

    # age purely entered to error handle hence no getter
    def set_age(self, age):
        '''Sets players age'''
        self.__age = age

    def set_body_type(self, body_type):
        '''Sets player body type'''
        self.__body_type = body_type

    def set_weapon(self, weapon):
        '''Sets player weapon type'''
        self.__weapon = weapon

    def damage(self, health):
        '''Deals damage to player health'''
        self.__health -= health

class ComputerPlayer(Player):
    '''Child Class of the Player Class for AI specifics'''
    # Random names for AI player
    bot_names = ["Terminator", "Annihilator", "Destroyer", "Crusher", "Nuts-n-Bolts", "Link",
    "Mechanicus", "Ripper", "Tank", "Shredder"]

    # Random Body type for AI player
    bot_body_type = ["Tracked", "Soft-Wheeled", "Hard-Wheeled"]

    # Random Arm weapon for AI player
    bot_weapon = ["Electrocutor", "Powersaw", "Flipper"]

    def __init__(self):
        self.__name = choice(ComputerPlayer.bot_names)
        self.__body_type = choice(ComputerPlayer.bot_body_type)
        self.__weapon = choice(ComputerPlayer.bot_weapon)
        self.__health = 120
        # Had to declare all parameters as body type and weapon were positional
        super().__init__(self.__name, self.__health, self.__body_type, self.__weapon)

class Game():
    '''Create a game object that instantiates all the components nescessary to play the game'''
    # Initilizes a main player and second player (either human or computer)
    def __init__(self):
        self.player_one = ""
        self.player_two = ""
        self.attack_first_flag = False
        self.arena_effects_flag = False
        self.game_exit_flag = False
        # Dmg calculator sets of tuples for calculating damage
        self.strong_against_weapon = {
            ("Electrocutor", "Flipper"),
            ("Powersaw", "Electrocutor"),
            ("Flipper", "Powersaw")
        }
        self.weak_against_weapon = {
            ("Electrocutor", "Electrocutor"),
            ("Powersaw", "Powersaw"),
            ("Flipper", "Flipper")
        }

        self.strong_against_body = {
            ("Electrocutor", "Tracked"),
            ("Powersaw", "Soft-Wheeled"),
            ("Flipper", "Hard-Wheeled")
        }
        self.weak_against_body = {
            ("Electrocutor", "Soft-Wheeled"),
            ("Powersaw", "Hard-Wheeled"),
            ("Flipper", "Tracked")
        }

        # creates a an art title that initilizes when a game object is created 
        self.menu_title = text2art("Battle Robots", font='block-medium', chr_ignore=True)
    #Initializes Colorama, if Windows  filter ANSI escape sequences out of any text
    #sent to stdout or stderr, and replace them with equivalent Win32 calls
    colorama.init(autoreset=True)

    def introduction(self):
        '''Intro message method for Battle Robots'''
        self.clear_terminal()
        print("... initializing...\n")
        sleep(2)
        # Unable to interpolate the Fore.RED from colorama into the below text2art
        title_art = text2art("Battle Robots !", font='block-medium', chr_ignore=True)
        print(Fore.RED + title_art)
        sleep(3)

    def clear_terminal(self):
        '''Method that clears the terminal throughout the game so players don't have to scroll'''
        system("cls" if name == "nt" else "clear")

    def weap_weap_dmg(self, first, second):
        '''Calculate damage for weapon attacking weapon'''
        if (first, second) in self.strong_against_weapon:
            return 30
        elif (first, second) in self.weak_against_weapon:
            return 10
        else:
            return 20

    def weap_body_dmg(self, first, second):
        '''Calculate damage for weapon attacking body'''
        if (first, second) in self.strong_against_body:
            return 30
        elif (first, second) in self.weak_against_body:
            return 10
        else:
            return 20

    def health_color(self, player):
        '''changes color of health depending on health returned'''
        if player.get_health() >= 80:
            return Fore.GREEN + str(player.get_health())
        elif player.get_health() >= 40 and player.get_health() < 80:
            return Fore.YELLOW + str(player.get_health())
        else:
            return Fore.RED + str(player.get_health())

    def game_mode(self):
        '''Game mode select menu that calls singleplayer or multiplayer methods'''
        self.clear_terminal()
        print(Fore.RED + self.menu_title)

        options = ["Single Player", "Multi Player", "Exit Game"]

        while True:
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()

            if menu_entry_index == 2:  # Exit Game
                print(f"You have selected {options[menu_entry_index]}!\n")
                break

            try:
                print(f"You have selected {options[menu_entry_index]}!\n")
                sleep(1)
                self.clear_terminal()
                if menu_entry_index == 0:
                    self.single_player()
                    self.game_exit_flag = False
                elif menu_entry_index == 1:
                    self.multi_player()
                    self.game_exit_flag = False
                self.clear_terminal()
                print(Fore.RED + self.menu_title)
            except Exception as e:
                print("An error occurred:", e)
                sleep(2)
                self.clear_terminal()
                print(Fore.RED + self.menu_title)
        
        # Uninitializes Colorama when game ends, restores stdout,stderr to original value on Windows
        colorama.deinit()

    def single_player(self):
        '''Single player method that creates a human and computer player, 
        calls arena effects method then body type method
        '''
        # Errors handled on input for blank entries
        print(Fore.RED + self.menu_title)        
        self.player_one = Player()
        while True:
            try:
                player_one_age = int(input("Please enter your age ? "))
                if player_one_age < 0:
                    print("Please enter a valid age")
                    sleep(1)
                    continue
                self.player_one.set_age(player_one_age)
                break
            except ValueError:
                print ("Please enter your age as a whole number")
                sleep(1.5)
                self.clear_terminal()
                print(Fore.RED + self.menu_title)
                continue           
        player_one_name = input("What's your Battle Robots Name ? ")
        self.player_one.set_name(player_one_name.capitalize())
        while len(self.player_one.get_name()) == 0:
            print("Cannot have a blank name..")
            sleep(2)
            self.clear_terminal()
            print(Fore.RED + self.menu_title)
            player_one_name = input("What's your Battle Robots Name ? ")
            self.player_one.set_name(player_one_name.capitalize()) 
        print(f"\n Welcome, {self.player_one.get_name()}")
        self.player_two = ComputerPlayer()
        print(f"\n You're Battling: {self.player_two.get_name()}!\n")
        print("...initializing...")
        sleep(4)
        self.clear_terminal()
        self.arena_effects()
        self.body_type_menu(self.player_one, self.player_two)

    def multi_player(self):
        '''Multiplayer method that creates two human players,
        calls arena effects method then body type method
        '''
        # Errors prevented on input for blank entries and same name for both players
        print(Fore.RED + self.menu_title)
        self.player_one = Player()
        player_one_name = input("Player One: What's your Battle Robots Name ? ")
        self.player_one.set_name(player_one_name.capitalize())
        self.clear_terminal()
        print(Fore.RED + self.menu_title)
        while len(self.player_one.get_name()) == 0:
            print("Cannot have a blank name..")
            sleep(2)
            self.clear_terminal()
            print(Fore.RED + self.menu_title)
            player_one_name = input("Player One: What's your Battle Robots Name ? ")
            self.player_one.set_name(player_one_name.capitalize())           
        self.player_two = Player() 
        player_two_name = input("Player Two: What's your Battle Robots Name ? ")
        self.player_two.set_name(player_two_name.capitalize())
        while self.player_one.get_name() == self.player_two.get_name() or len(self.player_two.get_name()) == 0:
            print("Both players cannot have the same name or blank names ")
            sleep(2)
            self.clear_terminal()
            print(Fore.RED + self.menu_title)
            player_two_name = input("Player Two: What's your Battle Robots Name ? ")
            self.player_two.set_name(player_two_name.capitalize())
        self.clear_terminal()
        self.arena_effects()
        self.body_type_menu(self.player_one, self.player_two)        

    def arena_effects(self):
        '''Arena effects menu, user can toggle on or off'''
        print(Fore.RED + self.menu_title)
        print("Do you want Arena Effects added to game ?\n")
        print(" Arena effects allow players to target their opponent with the Arena's Powersaw's, Crushing Mallets and Flame-Jets!\n")
        print(" Players may also randomly be hit by these effects in the Arena!\n")

        options = ["Yes", "No"]

        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        self.clear_terminal()
        if menu_entry_index == 0:
            print(f"You have selected {options[menu_entry_index]}!\n")
            self.arena_effects_flag = True
        elif menu_entry_index == 1:
            print(f"You have selected {options[menu_entry_index]}!\n")
            self.arena_effects_flag = False
        self.clear_terminal()

    def body_type_menu(self, player_one, player_two):
        '''Body type select menu, allows both players sequentially to select body,
        then calls weapon method
        '''
        print(Fore.RED + self.menu_title)
        players = [player_one, player_two]
        exit_flag = False
        for char in players:
            if isinstance(char, ComputerPlayer):
                self.weapon_menu(player_one, player_two)
            else:
                print(f"{char.get_name()}: What Body-Type do you want ? \n")

                body_type_options = ["Tracked", "Soft-Wheeled", "Hard-Wheeled", "Main Menu"]

                terminal_menu = TerminalMenu(body_type_options)
                menu_entry_index = terminal_menu.show()

                while menu_entry_index != 3:
                    try:
                        print(f"You have selected {body_type_options[menu_entry_index]}!\n")
                        if menu_entry_index == 0:
                            char.set_body_type("Tracked")
                        elif menu_entry_index == 1:
                            char.set_body_type("Soft-Wheeled")
                        elif menu_entry_index == 2:
                            char.set_body_type("Hard-Wheeled")
                        sleep(2)
                        self.clear_terminal()
                        print(Fore.RED + self.menu_title)
                        break
                    except TypeError:
                        print ("Please select an option...")
                        sleep(1)
                        self.clear_terminal()
                        print(Fore.RED + self.menu_title)
                        print(f"{char.get_name()}: What Body-Type do you want ? \n")
                        menu_entry_index = terminal_menu.show()
                        continue
                if menu_entry_index == 3:
                    exit_flag = True
                    self.clear_terminal()
                    print(Fore.RED + self.menu_title)
                    print(f"You have selected {body_type_options[menu_entry_index]}!\n")
                    sleep(1)
            if self.game_exit_flag:
                break
            if exit_flag:
                self.clear_terminal()
                break
        if exit_flag is False and self.game_exit_flag is not True:
            self.weapon_menu(player_one, player_two)

    def weapon_menu(self, player_one, player_two):
        '''Weapons select menu, allows both players sequentially to select weapons,
        then calls battle load screen method
        '''
        players = [player_one, player_two]
        exit_flag = False
        for char in players:
            # If computer player in game, auto selects their components
            if isinstance(char, ComputerPlayer):
                self.bot_select()
            else:
                print(f"{char.get_name()}: What Weapon do you want to punish your opponent with!\n")
                weapon_options = ["Electrocutor", "Powersaw", "Flipper", "Main Menu"]

                terminal_menu = TerminalMenu(weapon_options)
                menu_entry_index = terminal_menu.show()

                while menu_entry_index != 3:
                    try:
                        print(f"You have selected {weapon_options[menu_entry_index]}!\n")
                        if menu_entry_index == 0:
                            char.set_weapon("Electrocutor")                       
                        elif menu_entry_index == 1:
                            char.set_weapon("Powersaw")
                        elif menu_entry_index == 2:
                            char.set_weapon("Flipper")
                        sleep(2)
                        self.clear_terminal()
                        print(Fore.RED + self.menu_title)
                        break
                    except TypeError:
                        print ("Please select an option...")
                        sleep(1)
                        self.clear_terminal()
                        print(Fore.RED + self.menu_title)
                        print(f"{char.get_name()}: What Weapon do you want to punish your opponent with!\n")
                        menu_entry_index = terminal_menu.show()
                        continue   
                if menu_entry_index == 3:
                    exit_flag = True
                    self.clear_terminal()
                    print(Fore.RED + self.menu_title)
                    print(f"You have selected {weapon_options[menu_entry_index]}!\n")
                    sleep(1)
            if exit_flag:
                self.clear_terminal()
                self.game_exit_flag = True
                break
        if exit_flag is False:
            self.battle_load_screen()

    def bot_select(self):
        '''Computer player component auto select menu, called in weapons menu method'''
        print(f"{self.player_two.get_name()} is thinking....\n")
        sleep(2)
        print(f"{self.player_two.get_name()} has selected Body Type: {self.player_two.get_body_type()}\n")
        print(f"{self.player_two.get_name()} has selected Weapon: {self.player_two.get_weapon()}\n")
        print("...initializing...")
        sleep(4)
        self.clear_terminal()
        print(Fore.RED + self.menu_title)
    
    def battle_load_screen(self):
        '''Battle load screen method displays players selected attributes and randomly rolls for who attacks first,
        calls battle method
        '''
        print(Fore.BLUE + f"Player One: {self.player_one.get_name()}, Health: {self.player_one.get_health()}, Weapon: {self.player_one.get_weapon()}, Body-Type: {self.player_one.get_body_type()}\n")
        print(Fore.YELLOW + "VERSUS!\n")
        print(Fore.GREEN + f"Player Two: {self.player_two.get_name()}, Health: {self.player_two.get_health()}, Weapon: {self.player_two.get_weapon()}, Body-Type: {self.player_two.get_body_type()}\n")
        print("...initializing...\n")
        sleep(4)
        self.clear_terminal()
        print(Fore.RED + self.menu_title)
        print("Roll for who attacks first!\n")
        player_one_roll = 0
        player_two_roll = 0
        while player_one_roll == player_two_roll:
            player_one_roll = randint(1, 6)
            print(f"{self.player_one.get_name()} rolls: {player_one_roll}\n")
            player_two_roll = randint(1, 6)
            print(f"{self.player_two.get_name()} rolls: {player_two_roll}\n")
            if player_one_roll == player_two_roll:
                print("Same number, roll again!\n")
                continue
            elif player_one_roll > player_two_roll:
                print(f"{self.player_one.get_name()} attacks first!\n")
                self.attack_first_flag = False
                break
            elif player_two_roll > player_one_roll:
                print(f"{self.player_two.get_name()} attacks first!\n")
                self.attack_first_flag = True
                break
        print("...initializing...\n")
        sleep(5)
        self.clear_terminal()        
        # Flag variable called in game object that determines who goes first based on roll above
        # Battle method called in here
        if self.attack_first_flag is True:
            self.battle(self.player_two, self.player_one)
        elif self.attack_first_flag is False:
            self.battle(self.player_one, self.player_two)
        # self.player_two

    def battle(self, first, second):
        '''Large Battle method that allows players to sequentially attack each other,
        includes computer attack and Arena attacks
        '''
        # Declared menu variable here to prevent assignment errors later (required two menus one for bot and one for players)
        print(Fore.RED + self.menu_title)
        menu_entry_index = True
        bot_entry_index = True
        while self.player_one.get_health() > 0 and self.player_two.get_health() > 0: 
            print(f"Player One: {self.player_one.get_name()}, Health: {self.health_color(self.player_one)}")
            print(f"Weapon: {self.player_one.get_weapon()}, Body-Type: {self.player_one.get_body_type()}\n")
            print(f"Player Two: {self.player_two.get_name()}, Health: {self.health_color(self.player_two)}")
            print(f"Weapon: {self.player_two.get_weapon()}, Body-Type: {self.player_two.get_body_type()}\n")
            print("Where do you want to attack your opponent, " f"{first.get_name()}?\n")
            # List of attack options for players below (only 2 when declared, weapons and body type)
            attack_options = [f"Attack {second.get_name()} Weapon: {second.get_weapon()} ", f"Attack {second.get_name()} Body: {second.get_body_type()} "]
            # Arena effects added here, arena options declared outside if statement so they can be used later in random attack statement
            arena_options = ["Powersaw", "Crushing Mallets", "Flame-Jets"]
            arena_choice = choice(arena_options)
            if self.arena_effects_flag:
                # Adds a 3rd attack option to list
                attack_options += [f"Attempt to push {second.get_name()} into the Arena's {arena_choice}"]           
            # Bot specific attack menu
            if isinstance(first, ComputerPlayer):
                bot_entry_index = choice(attack_options)
                sleep(2)
                print(f"{first.get_name()} is thinking....\n")
                sleep(3)
                if bot_entry_index == attack_options[0]:
                    print(f"{first.get_name()} has selected: Attack {second.get_name()} Weapon: {second.get_weapon()}\n")
                    sleep(3)
                elif bot_entry_index == attack_options[1]:
                    print(f"{first.get_name()} has selected: Attack {second.get_name()} Body: {second.get_body_type()}\n")
                    sleep(3)
                elif bot_entry_index == attack_options[2]:
                    print(f"{first.get_name()} attempts to push {second.get_name()} into the Arena's {arena_choice}\n")
                    sleep(3)
            # Human player menu
            else:
                terminal_menu = TerminalMenu(attack_options)
                menu_entry_index = terminal_menu.show()

                print(f"You have selected {attack_options[menu_entry_index]}\n")
                sleep(2)
            # Weapon always attacks either body or Weapon
            # Dmg calculator for Weapon attacking Weapon, calls weapon v weapon method
            if menu_entry_index == 0 or bot_entry_index == attack_options[0]:
                damage_taken = self.weap_weap_dmg(first.get_weapon(), second.get_weapon())
                second.damage(damage_taken)
            # Dmg calculator for Weapon attacking Body, calls weapon v body method
            elif menu_entry_index == 1 or bot_entry_index == attack_options[1]:
                damage_taken = self.weap_body_dmg(first.get_weapon(), second.get_body_type())
                second.damage(damage_taken)
            #  If Random Arena attack selected
            elif menu_entry_index == 2 or bot_entry_index == attack_options[2]:
                damage_taken = randint(0, 40)
                second.damage(damage_taken)
            print(f"{second.get_name()} takes {damage_taken} damage!\n")
            # Random Arena damage to a random player
            if self.arena_effects_flag:
                player_chance = [first, second]
                # random pick of players in game
                player_attacked = choice(player_chance)
                # random damage between 0 - 20
                rand_attack_dmg = randint(0, 20)
                random_chance = randint(0, 100)
                # 25% chance of player taking damage
                if random_chance <= 25:
                    arena_choice = choice(arena_options)
                    sleep(2)                    
                    print(f"{player_attacked.get_name()} has driven into the Arena's {arena_choice}!\n")
                    sleep(2)
                    print(f"{player_attacked.get_name()} takes {rand_attack_dmg} damage! ouch...\n")
                    player_attacked.damage(rand_attack_dmg)
                    sleep(2)
            sleep(2)
            self.clear_terminal()
            print(Fore.RED + self.menu_title)
            first, second = second, first
        if self.player_one.get_health() > 0:
            print(f"\n{self.player_one.get_name()} has obliterated {self.player_two.get_name()} in the Arena!\n")
            print(Fore.RED + f"\n{self.player_one.get_name()} Wins!\n")
        else:
            print(f"\n{self.player_two.get_name()} has obliterated {self.player_one.get_name()} in the Arena!\n")
            print(Fore.RED + f"\n{self.player_two.get_name()} Wins!\n")
        sleep(4)
        self.game_exit_flag = True
        self.clear_terminal()
