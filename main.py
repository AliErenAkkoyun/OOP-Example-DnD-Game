"""
In this project, my main purpose is to create functional D&D script using OOP methodologies.
Few features may be missing, like leveling up and saving the progress, so please be patient.


D4-D6-D8-D10-D12-D20-D100 ---> This methods can be usable for every character. They will inherit it, but in the
calculations the STATS will affect them, so this is not the final point in a throw.

The Initiations ---> Before anything else, I need to make the characters and their blueprints. So everything will
start within another .py file and I get the required information to make the character.
First the race and class, then stats.

CHARACTER
    Race - Class - Hp - Weapons - Stats - Equipment - Attack - Background
    Race & Class ---> You pick them. They have their advantages and disadvantages.
    Stats ---> STR , DEX , CON , INT , WIS , CHR  # The stat determination is explained later.
               The Stats have not been affected by race and class yet.
    Hp ---> Max damage point(Determined by your class) + CON
    Equipment ---> The armours and other stuff, like consumables, you have.
    Attack ---> Weapons and the attack styles you have. Scales with STATS.
        Weapons ---> The weapons you have.
    Background ---> The text. Maybe change later IDK.
"""

# TODO: Complete the entire Mechanics methods
# 1-: Complete the character creation process
# 2-: Add weaponry and sorcery to the class part
# 3-: Add hit mechanic (related with health and damage mechanic)
# 4-: Leveling up precesses

from random import randint
from operator import add


class Mechanics:
    @staticmethod
    def _character_initiator(race, character_class):
        """
        This method helps you to create the core concepts of a character, "Race" and "Class". This method
        specifically used inside the "character_creator" method.
        :param race: "Human", "Elf", "Orc". Gives you specific stat bonuses for each race.
        :param character_class: "Warrior", "Sorcerer", "Rogue". The class you pick, but this is not complete now.
        :return: Gives the race stat bonuses. May give weaponry and gear later.
        """
        try:
            the_thing = []
            race_bonus = [0, 0, 0, 0, 0, 0]  # STR DEX CON INT WIS CHR
            if race == "1":
                the_thing.append("Human")
                race_bonus = [1, 1, 1, 1, 1, 1]
            elif race == "2":
                the_thing.append("Elf")
                race_bonus = [0, 2, 0, 1, 1, 0]  # Stats may look unfair, cry about it.
            elif race == "3":
                the_thing.append("Orc")
                race_bonus = [2, 0, 2, 0, 0, 0]

            if character_class == "1":
                the_thing.append("Warrior")
            elif character_class == "2":
                the_thing.append("Sorcerer")
            elif character_class == "3":
                the_thing.append("Rogue")

            print(f"You picked the {the_thing[0]} race and {the_thing[1]} class")

            return race_bonus
        except Exception as err:
            print("Someting went wrong: ", err)

    @staticmethod
    def roll_dice(dice_type, amount, operation_type: str = "Add"):
        """
        Roll a die with specified parameters. Like, d{dice_type} = d4.
        Example:  roll_dice(4,6, "Add") =  roll d4 dice 6 times and add the rolled numbers.
        :param dice_type: D4, D6, D10 etc. You can specify a nonexistent dice tipe like D37 or smt
        :param amount: How many times does this die needs to be rolled.
        :param operation_type: Add the rolled dice values or give them as List. "Add" for adding "List" for listing
        :return: Returns the sum of the all dice rolled.
        """
        try:
            raw_roll = []

            for i in range(amount):
                dice_roll = randint(1, dice_type)
                raw_roll.append(dice_roll)

            if operation_type == "List":
                return raw_roll
            elif operation_type == "Add":
                return sum(raw_roll)
        except Exception as err:
            print("Something went wrong: ",err)

    def stat_roll(self):
        """
        Makes the necessary dice rolling for stat declaration. Asks for the stat placement to the user. There are no
        recommendations for class stats. User can give any number that is in the pool to any stat.
        :return: Returns the final version of the stats wrt. this order: STR | DEX | CON | INT | WIS | CHR
        """
        try:
            cal_dice = [0, 0, 0, 0, 0, 0]
            stats = [0, 0, 0, 0, 0, 0]
            for i in range(0, 6):
                cal_dice[i] = self.roll_dice(6, 4, "List")
                cal_dice[i].remove(min(cal_dice[i]))
                cal_dice[i] = sum(cal_dice[i])

            stat_names = ["STR", "DEX", "CON", "INT", "WIS", "CHR"]
            stat_holder = 0
            for i in range(0, 6):
                if i == 0:
                    stat_holder = input(f"Your Stat Pool is \n {cal_dice} \n Now please select the {stat_names[i]} stat")
                    stats[i] = int(stat_holder)
                else:
                    cal_dice.remove(int(stat_holder))
                    print(cal_dice)
                    stat_holder = input(f"Your current Stats are \n {stats} \n "
                                        f"Your remaining Stat Pool is \n {cal_dice} \n "
                                        f"Now please select the {stat_names[i]} stat")
                    stats[i] = int(stat_holder)

            stats = list(map(add, stats, self.race_bonus))
            return stats

        except Exception as err:
            print("Something went wrong: ",err)

    def ability_modifier(self):
        pass

    def character_creator(self):
        """
        Creates the character wrt. user inputs. Uses other methods to do so.
        :return: Returns the finalised character stats.
        """
        try:
            race = input("Hello, please select your Race: \n 1-Human \n 2-Elf \n 3-Orc")
            character_class = input("Now please select your Class: \n 1-Warrior \n 2-Sorcerer \n 3-Rogue")
            self.race_bonus = self._character_initiator(race, character_class)
            print(f"Your race bonus is {self.race_bonus}. \n Now lets roll for stats")
            character_stats = list(map(add, self.race_bonus, self.stat_roll()))
            return character_stats
        except Exception as err:
            print("Something went wrong: ", err)


""" Cemetery (may come back to life/spare codes)
STR | DEX | CON | INT | WIS | CHR  
"""
