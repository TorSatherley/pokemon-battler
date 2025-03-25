class Pokemon:
    def __init__(self, name, hit_points, attack_damage, move):
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.move = move

    def use_move(self):
        return f'{self.name} used {self.move}!'
    
    def take_damage(self, damage_taken):
        self.hit_points -= damage_taken 

    def has_fainted(self):
        if self.hit_points < 1:
            return True
        return False

class Fire(Pokemon):
    def __init__(self, name, hit_points, attack_damage, move):
        super().__init__(name, hit_points, attack_damage, move)
        self.type = 'Fire'
        self.strong_against = 'Grass'
        self.weak_against = 'Water'

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
        self.type = 'Water'
        self.strong_against = 'Fire'
        self.weak_against = 'Grass'

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
        self.type = 'Grass'
        self.strong_against = 'Water'
        self.weak_against = 'Fire'

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
        self.type = 'Normal'
        self.strong_against = None
        self.weak_against = None

    def get_multiplier(self, opponent):
        return 1


class Pokeball():
    def __init__(self):
        self.stored_pokemon = None

    def catch(self, Pokemon):
        if self.stored_pokemon == None:
            self.stored_pokemon = Pokemon
        else:
            return "Pokeball isn't empty!" # improvement - raise as exception

    def is_empty(self):
        if self.stored_pokemon == None:
            return True
        return False

class Trainer():  
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
            self.pokeball6
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
            return 'Belt is full!' # improvement - raise as exception

class Battle():
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
            self.turn_counter +=1
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
            return f'{defender.name} has fainted! {attacker.name} has won!'
        else:
            return None
        

    #

