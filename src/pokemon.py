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


class Pokeball(Pokemon):
    def __init__(self, stored_pokemon = None):
        self.stored_pokemon = stored_pokemon

    def catch(self, Pokemon):
        if self.stored_pokemon == None:
            self.stored_pokemon = Pokemon
        
    
    def is_empty(self):
        if self.stored_pokemon == None:
            return True
        return False
    
class Trainer(Pokeball):
    
    def __init__(self):
        self.trainer_belt = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
        self.available_balls = 6

    def throw_pokeball(self, Pokemon):
        if self.available_balls > 0 and self.available_balls <= 6:
            for ball,value in self.trainer_belt.items():
                if value == None:
                    self.trainer_belt[ball] = Pokemon
                    self.available_balls -= 1
                    break
            else:
                return 'Belt is full!'  
            # Pokeball.catch(Pokemon)
            # self.available_balls -= 1

#create a belt with max 6 balls
#each throw pokeball will alocate a pokemon to a ball
#loop through each ball and check if empty
#if is empty then catch
