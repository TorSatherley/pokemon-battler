class Pokemon:
    def __init__(self, name, hit_points, attack_damage, move):
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.move = move

    def use_move(self):
        return f'{self.name} used {self.move}'
    
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


class Pokeball:
    def __init__(self):
        self.stored_pokemon = None

    def catch(self, Pokemon):
        if self.stored_pokemon == None:
            self.stored_pokemon = Pokemon
        return self.stored_pokemon
    
    def is_empty(self):
        if self.stored_pokemon == None:
            return True
        return False
    