from tabulate import tabulate


class Pokemon:
    def __init__(self, name, hit_points, attack_damage, move):
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.move = move

    def use_move(self):
        return f"{self.name} used {self.move}!"

    def take_damage(self, damage_taken):
        self.hit_points -= damage_taken

    def has_fainted(self):
        if self.hit_points < 1:
            return True
        return False


class Fire(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "Fire"
        self.strong_against = "Grass"
        self.weak_against = "Water"

    def get_multiplier(self, opponent):
        if self.strong_against == opponent.type:
            return 1.5
        elif self.weak_against == opponent.type:
            return 0.5
        else:
            return 1


class Water(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "Water"
        self.strong_against = "Fire"
        self.weak_against = "Grass"

    def get_multiplier(self, opponent):
        if self.strong_against == opponent.type:
            return 1.5
        elif self.weak_against == opponent.type:
            return 0.5
        else:
            return 1


class Grass(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "Grass"
        self.strong_against = "Water"
        self.weak_against = "Fire"

    def get_multiplier(self, opponent):
        if self.strong_against == opponent.type:
            return 1.5
        elif self.weak_against == opponent.type:
            return 0.5
        else:
            return 1


class Normal(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = "Normal"
        self.strong_against = None
        self.weak_against = None

    def get_multiplier(self, opponent):
        return 1


class Pokeball:
    def __init__(self):
        self.stored_pokemon = None

    def catch(self, Pokemon):
        if self.stored_pokemon == None:
            self.stored_pokemon = Pokemon
        else:
            return "Pokeball isn't empty!"  # improvement - raise as exception

    def is_empty(self):
        if self.stored_pokemon == None:
            return True
        return False


class Trainer:
    def __init__(self):
        self.pokeball1 = Pokeball()
        self.pokeball2 = Pokeball()
        self.pokeball3 = Pokeball()
        self.pokeball4 = Pokeball()
        self.pokeball5 = Pokeball()
        self.pokeball6 = Pokeball()
        self.trainer_belt = [
            self.pokeball1,
            self.pokeball2,
            self.pokeball3,
            self.pokeball4,
            self.pokeball5,
            self.pokeball6,
        ]
        self.available_balls = 6

    def throw_pokeball(self, Pokemon):
        if self.available_balls > 0 and self.available_balls <= 6:
            for pokeball in self.trainer_belt:
                if pokeball.is_empty():
                    pokeball.catch(Pokemon)
                    self.available_balls -= 1
                    break
        else:
            return "Belt is full!"  # improvement - raise as exception


class Battle:
    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.turn_counter = 1

    def take_turn(self):
        if self.turn_counter == 1:
            self.damage_taken(self.pokemon_1, self.pokemon_2)
            winner = self.get_winner(self.pokemon_1, self.pokemon_2)
            if winner is not None:
                return winner
            self.turn_counter += 1
        else:
            self.damage_taken(self.pokemon_2, self.pokemon_1)
            winner = self.get_winner(self.pokemon_2, self.pokemon_1)
            if winner is not None:
                return winner
            self.turn_counter -= 1

    def damage_taken(self, attacker, defender):

        total_damage = int(attacker.get_multiplier(defender) * attacker.attack_damage)
        defender.hit_points -= total_damage

    def get_winner(self, attacker, defender):
        if defender.has_fainted():
            return f"{defender.name} is down to {defender.hit_points} hit points, and has fainted! {attacker.name} has won!"
        else:
            return None


def run_pokemon_battler():

    print("Welcome to Pokemon Battler!")
    print(
        "Let's start by getting the names of the two trainers who will be battling today."
    )
    trainer_1 = str(input("Trainer 1 Name: "))
    trainer_2 = str(input("Trainer 2 Name: "))
    pokemon_data, pokemon_headers = pokemon_table()
    print(tabulate((pokemon_data), headers=pokemon_headers))

    choice_num_1 = get_pokemon_id(trainer_1)
    trainer_1_pokemon = get_pokemon_class(pokemon_data, choice_num_1)

    choice_num_2 = get_pokemon_id(trainer_2)
    trainer_2_pokemon = get_pokemon_class(pokemon_data, choice_num_2)

    print(
        f"{trainer_1}, your pokemon {trainer_1_pokemon.name} will now battle with {trainer_2}'s pokemon {trainer_2_pokemon.name}!"
    )
    battle = Battle(trainer_1_pokemon, trainer_2_pokemon)

    while battle.take_turn() is None:
        print(f"{trainer_1_pokemon.name} has {trainer_1_pokemon.hit_points} hit points left!")
        print(f"{trainer_2_pokemon.name} has {trainer_2_pokemon.hit_points} hit points left!")
    winning_statement = battle.take_turn()
    print(winning_statement)
    pass


def get_pokemon_id(trainer):
    num_choice = int(input(f"{trainer}, please enter the ID of your chosen Pokemon: "))
    while num_choice < 1 or num_choice > 7:
        print(f"{num_choice} is not a valid Pokemon ID.")
        num_choice = int(input("Please enter the ID of your chosen Pokemon: "))
    return num_choice


def get_pokemon_class(pokemon_data, choice_num):
    trainer_pokemon = {
        "type": pokemon_data[choice_num - 1][2],
        "name": pokemon_data[choice_num - 1][1],
        "hit_points": pokemon_data[choice_num - 1][3],
        "attack_damage": pokemon_data[choice_num - 1][5],
        "move": pokemon_data[choice_num - 1][4],
    }

    attributes = (
        trainer_pokemon["name"],
        trainer_pokemon["hit_points"],
        trainer_pokemon["attack_damage"],
        trainer_pokemon["move"],
    )

    if trainer_pokemon["type"] == "Normal":
        pokemon_instance = Normal(*attributes)
    elif trainer_pokemon["type"] == "Fire":
        pokemon_instance = Fire(*attributes)
    elif trainer_pokemon["type"] == "Water":
        pokemon_instance = Water(*attributes)
    elif trainer_pokemon["type"] == "Grass":
        pokemon_instance = Grass(*attributes)
    return pokemon_instance


def pokemon_table():
    pokemon_data = [
        [1, "Eevee", "Normal", 55, "Headbutt", 18, "None", "Fighting", "Eev... Eevee!"],
        [
            2,
            "Flareon",
            "Fire",
            65,
            "Fire blast",
            20,
            "Grass",
            "Water",
            "Eev... Fla... Flareon!",
        ],
        [
            3,
            "Vaporeon",
            "Water",
            70,
            "Hydro pump",
            19,
            "Fire",
            "Grass",
            "Vap... Vaporeon!",
        ],
        [
            4,
            "Leafeon",
            "Grass",
            65,
            "Giga drain",
            17,
            "Water",
            "Fire",
            "Lea... Leafeon!",
        ],
        [
            5,
            "Charmander",
            "Fire",
            44,
            "Flamethrower",
            17,
            "Grass",
            "Water",
            "Cha... Charmander!",
        ],
        [6, "Squirtle", "Water", 44, "Surf", 16, "Fire", "Grass", "Squ... Squirtle!"],
        [
            7,
            "Bulbasaur",
            "Grass",
            45,
            "Razor leaf",
            16,
            "Water",
            "Fire",
            "Bul... Bulbasaur!",
        ],
    ]
    pokemon_headers = [
        "Pokemon ID",
        "Name",
        "Type",
        "Hitpoints",
        "Move",
        "Damage",
        "Strength",
        "Weakness",
        "Sound",
    ]
    return pokemon_data, pokemon_headers


if __name__ == "__main__":
    run_pokemon_battler()
