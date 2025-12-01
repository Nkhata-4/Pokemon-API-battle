"""
Exercise 3.2: Simulate a Turn-Based Battle (Class-Based)

In this exercise, you will create a Pokemon class and use it to simulate battles.
This demonstrates object-oriented programming principles: encapsulation, methods, and clear responsibilities.
"""
import json
import httpx


class Pokemon:
    """
    Represents a Pokemon with stats fetched from the PokeAPI.
    """

    def __init__(self, name):
        self.name = name
        """
        Initialise a Pokemon by fetching its data from the API and calculating its stats.

        Args:
            name (str): The name of the Pokemon (e.g., "pikachu")
        """
        # TODO: Store the Pokemon's name (lowercase)


        # TODO: Fetch Pokemon data from PokeAPI
        # - Create the URL: f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        # - Make GET request
        # - Check response status code (raise error if not 200)
        # - Store the JSON data
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        stat_data = []
        response = httpx.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Get request was unsuccessful")
        # TODO: Calculate and store stats
        # - Use _calculate_stat() for attack, defense, speed
        # - Use _calculate_hp() for max HP
        # - Store stats in a dictionary
        # - Set current_hp = max_hp    
        stat_data = data['stats']
        for item in stat_data:
            if item['stat']['name'] == "hp":
                max_hp = item['base_stat']
            elif item['stat']['name'] == "attack":
                attack = item['base_stat']
            elif item['stat']['name'] == "defense":
                defense = item['base_stat']
            elif item['stat']['name'] == "special-attack":
                special_attack = item['base_stat']
            elif item['stat']['name'] == "special-defense":
                special_defense = item['base_stat']
            elif item['stat']['name'] == "speed":
                speed = item['base_stat']
            else:
                print("error")

        self.current_hp = max_hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    
        
        pass

    def _calculate_stat(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's stat at a given level.
        Helper method (note the underscore prefix).

        Args:
            base_stat (int): The base stat value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated stat
        """
        # TODO: Implement the stat calculation formula
        # Formula: int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)
        self.base_stat = base_stat
        self.level = level
        self.iv = iv
        self.ev = ev
        base_stat = int(((2 * self.base_stat + self.iv + (self.ev / 4)) * self.level / 100) + 5)
        
        return base_stat


    def _calculate_hp(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's HP at a given level.
        HP uses a different formula than other stats.

        Args:
            base_stat (int): The base HP value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated HP
        """
        # TODO: Implement the HP calculation formula
        # Formula: int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)
        self.current_hp = base_stat
        self.level = level
        self.iv = iv
        self.ev = ev
        self.current_hp = int(((2 * self.current_hp + self.iv + (self.ev / 4)) * self.level / 100) + self.level + 10)
        return self.current_hp

    def deal_damage(self, defender):
        """
        Attack another Pokemon, dealing damage based on stats.

        Args:
            defender (Pokemon): The Pokemon being attacked

        Returns:
            int: The amount of damage dealt
        """
        # TODO: Calculate damage using the damage formula
        # Formula: int((((2 * 50 * 0.4 + 2) * self.stats['attack'] * 60) / (defender.stats['defense'] * 50)) + 2)
        # Where 50 is level and 60 is base_power
        damage = int((((2 * 50 * 0.4 + 2) * self.attack * 60) / (defender.defense * 50)) + 2)

        # TODO: Make the defender take damage
        # Call defender.take_damage(damage)
        defender.take_damage(damage)
        return damage

        # TODO: Return the damage amount

    def take_damage(self, damage):
        """
        Reduce this Pokemon's HP by the damage amount.

        Args:
            amount (int): The damage to take
        """
        self.amount = damage
        self.current_hp = self.current_hp - self.amount
        if self.current_hp <= 0:
            print(f"{self.name} has fainted")
            self.current_hp = 0
        return self.current_hp
        # TODO: Reduce current_hp by amount
        # Make sure HP doesn't go below 0

    def is_fainted(self):
        """
        Check if this Pokemon has fainted (HP <= 0).

        Returns:
            bool: True if fainted, False otherwise
        """
        if self.current_hp <= 0:
            verdict = True
        else:
            verdict = False
        return verdict
        
        # TODO: Return True if current_hp <= 0, False otherwise

    def __str__(self):
        """
        String representation of the Pokemon for printing.

        Returns:
            str: A nice display of the Pokemon's name and HP
        """
        # TODO: Return a string like "Pikachu (HP: 95/120)"
        return f"{self.name} (HP: {self.current_hp}/{self.max_hp})"


def simulate_battle(pokemon1_name, pokemon2_name):
    """
    Simulate a turn-based battle between two Pokemon.

    Args:
        pokemon1_name (str): Name of the first Pokemon
        pokemon2_name (str): Name of the second Pokemon
    """
    # TODO: Create two Pokemon objects
    pokemon1 = Pokemon(pokemon1_name)
    pokemon2 = Pokemon(pokemon2_name)

    pokemon1.max_hp = pokemon1._calculate_hp(pokemon1.max_hp)
    pokemon2.max_hp = pokemon2._calculate_hp(pokemon2.max_hp)

    pokemon1.attack = pokemon1._calculate_stat(pokemon1.attack)
    pokemon2.attack = pokemon2._calculate_stat(pokemon2.attack)

    pokemon1.defense = pokemon1._calculate_stat(pokemon1.defense)
    pokemon2.defense = pokemon2._calculate_stat(pokemon2.defense)

    pokemon1.speed = pokemon1._calculate_stat(pokemon1.speed)
    pokemon2.speed = pokemon2._calculate_stat(pokemon2.speed)
    


    # TODO: Display battle start message
    # Show both Pokemon names and initial HP
    print(f"This is a fierce battle between {pokemon1.name} and {pokemon2.name}!")
    print(f"{pokemon1.name}, HP: {pokemon1.max_hp}")
    print(f"{pokemon2.name}, HP: {pokemon2.max_hp}")

    # TODO: Determine who attacks first based on speed
    # The Pokemon with higher speed goes first
    # Hint: Compare pokemon1.stats['speed'] with pokemon2.stats['speed']
    if pokemon1.speed >= pokemon2.speed:
        winner = pokemon1
        defender = pokemon2
        print(f"{winner.name} attacks first!")
    else:
        winner = pokemon2
        defender = pokemon1
        print(f"{winner.name} attacks first")


    # TODO: Battle loop
    # - Keep track of round number
    # - While neither Pokemon is fainted:
    #   - Display round number
    #   - Attacker attacks defender
    #   - Display damage and remaining HP
    #   - Check if defender fainted
    #   - If not, swap attacker and defender
    #   - Increment round number
    i = 1
    while pokemon1.is_fainted() == False and pokemon2.is_fainted() == False:
        print(f"This is round {i}!")
        if i % 2 != 0:
            print(f"{winner.name} is now attacking!")
            winner.deal_damage(defender)
            print(winner)
            print(defender)
            i = i + 1
        else:
            print(f"{defender.name} is now attacking!")
            defender.deal_damage(winner)
            print(defender)
            print(winner)
            i = i + 1
            
    print("The match has ended")
    if pokemon1.is_fainted() == False:
        print(f"The winning pokemon is {pokemon1.name} with HP= {pokemon1.current_hp}!")
    else:
        print(f"The winning pokemon is {pokemon2.name} with HP= {pokemon2.current_hp}!")
    


    # TODO: Display battle result
    # Show which Pokemon won and their remaining HP
    pass


if __name__ == "__main__":
    # Test your battle simulator
    simulate_battle("pikachu", "bulbasaur")

    # Uncomment to test other battles:
    # simulate_battle("charmander", "squirtle")
    # simulate_battle("eevee", "jigglypuff")
