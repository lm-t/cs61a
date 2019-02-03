"""The Pokemon class below is an example of an application of
object-oriented programming, used to introduce and demonstrate
the various principles of OOP. It is a very simplified
implementation of the popular Japanese Pokemon games, distributed
by Nintendo. Every instance of this class represents
a single Pokemon.

Written by Jon Kotker and Tom Magrino in Summer 2012.
"""

import os
def clear():
    os.system('clear')
    return None


class Pokemon:
    """Class variables"""
    total_pokemon = 0
    trainer_dir = {}

    def __init__(self, name, owner, hit_pts):
        """Constructor."""
        self.name = name            # Name of the Pokemon.
        self.owner = owner          # Owner of the Pokemon.
        self.hp = hit_pts           # Hit points (HP) of the Pokemon.
        Pokemon.total_pokemon += 1  # Total number of Pokemon.

        if name not in Pokemon.trainer_dir:
            Pokemon.trainer_dir[name] = [owner]
        else:
            Pokemon.trainer_dir[name].append(owner)

    def increase_hp(self, amount):
        """Increase the hit points of a Pokemon."""
        self.hp += amount
    def decrease_hp(self, amount):
        """Decrease the hit points of a Pokemon,
        ensuring that the hit points never goes down below zero."""
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def attack(self, other):
        """Attack another Pokemon, after screaming the name."""
        print(self.get_name() + "!")
        other.decrease_hp(50)

    def get_name(self):
        return self.name
    def get_owner(self):
        return self.owner
    def get_hit_pts(self):
        return self.hp

    @property
    def complete_name(self):
        """Return the complete name of the Pokemon.
        This serves as an example of a property."""
        return self.get_owner() + "'s " + self.get_name()

    def __gt__(self, other):
        """Redefine the greater-than (>) operator, allowing
        two Pokemon to be compared using their hit points."""
        return self.get_hit_pts() > other.get_hit_pts()
    def __eq__(self, other):
        """Redefine the equality (==) operator, allowing
        two Pokemon to be equal if they have the same number of hit points."""
        return self.get_hit_pts() == other.get_hit_pts()

    @staticmethod
    def trainers(name):
        """Returns a list of the trainers that own the Pokemon with
        the name provided."""
        if name in Pokemon.trainer_dir:
            return Pokemon.trainer_dir[name]
        return None

class ElectricPokemon(Pokemon):
    """Subclass of the Pokemon class for Electric Pokemon."""
    def attack(self, other):
        # Example of using a method from the parent class.
        Pokemon.attack(self, other)
        self.increase_hp(10)

class WaterPokemon(Pokemon):
    """Subclass of the Pokemon class for Water Pokemon."""
    def attack(self, other):
        print(self.get_name() + "!")
        other.decrease_hp(75)

"""A few sample Pokemon for demonstration.
HP values obtained from www.pokedream.com."""
mistys_togepi = Pokemon('Togepi', 'Misty', 245)
ashs_pikachu = ElectricPokemon('Pikachu', 'Ash', 300)
brocks_pikachu = ElectricPokemon('Pikachu', 'Brock', 300)
ashs_squirtle = WaterPokemon('Squirtle', 'Ash', 314)
