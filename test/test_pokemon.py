from src.pokemon import Pokemon,Fire,Water,Grass,Normal,Pokeball

class TestProperties:
    def test_eevee_returns_relevant_properties(self):
        test_pokemon = Pokemon('Eevee', 55, 18, 'Headbut')
        assert test_pokemon.name == 'Eevee'
        assert test_pokemon.hit_points == 55
        assert test_pokemon.attack_damage == 18
        assert test_pokemon.move == 'Headbut'
    
class TestMethods:
    def test_use_move_returns_string(self):
        test_pokemon = Pokemon('Eevee', 55, 18, 'Headbut')
        assert test_pokemon.use_move() == 'Eevee used Headbut'

    def test_takes_damage_reduces_health_by_attack_damage(self):
        test_pokemon = Pokemon('Eevee', 55, 18, 'Headbut')
        test_pokemon.take_damage(20)
        assert test_pokemon.hit_points == 35

    def test_has_fainted_happens_when_health_hits_zero(self):
        test_pokemon = Pokemon('Eevee', 55, 18, 'Headbut')
        test_pokemon.take_damage(55)
        assert test_pokemon.has_fainted() == True
        
    def test_has_fainted_happends_when_health_below_zero(self):
        test_pokemon = Pokemon('Eevee', 55, 18, 'Headbut')
        test_pokemon.take_damage(60)
        assert test_pokemon.has_fainted() == True

    def test_has_fainted_returns_false_when_health_above_zero(self):
        test_pokemon = Pokemon('Eevee', 55, 18, 'Headbut')
        test_pokemon.take_damage(50)
        assert test_pokemon.has_fainted() == False

class TestTypes:
    def test_fire_type_inherites_from_base_class(self):
        test_pokemon = Fire('Flareon', 65, 20, 'Fire blast')
        assert test_pokemon.name == 'Flareon'
        assert test_pokemon.hit_points == 65
        assert test_pokemon.attack_damage == 20
        assert test_pokemon.move == 'Fire blast'

    def test_Grass_type_inherites_from_base_class(self):
        test_pokemon = Grass('Leafeon', 65, 17, 'Giga drain')
        assert test_pokemon.name == 'Leafeon'
        assert test_pokemon.hit_points == 65
        assert test_pokemon.attack_damage == 17
        assert test_pokemon.move == 'Giga drain'

    def test_water_type_inherites_from_base_class(self):
        test_pokemon = Fire('Vaporeon', 70, 19, 'Hydro pump')
        assert test_pokemon.name == 'Vaporeon'
        assert test_pokemon.hit_points == 70
        assert test_pokemon.attack_damage == 19
        assert test_pokemon.move == 'Hydro pump'

    def test_normal_type_inheries_from_base_class(self):
        test_pokemon = Pokemon('Eevee', 55, 18, 'Headbut')
        assert test_pokemon.name == 'Eevee'
        assert test_pokemon.hit_points == 55
        assert test_pokemon.attack_damage == 18
        assert test_pokemon.move == 'Headbut'

    def test_multiplier_function_works_water(self):
        test_pokemon = Water('Vaporeon', 70, 19, 'Hydro pump')
        test_opponent = Fire('Flareon', 65, 20, 'Fire blast')
        test_opponent1 = Grass('Leafeon', 65, 17, 'Giga drain')
        test_opponent2 = Normal('Eevee', 55, 18, 'Headbut')
        assert test_pokemon.get_multiplier(test_opponent) == 1.5
        assert test_pokemon.get_multiplier(test_opponent1) == 0.5
        assert test_pokemon.get_multiplier(test_opponent2) == 1
    
    def test_multiplier_function_works_fire(self):
        test_pokemon = Fire('Flareon', 65, 20, 'Fire blast')
        test_opponent = Water('Vaporeon', 70, 19, 'Hydro pump')
        test_opponent1 = Grass('Leafeon', 65, 17, 'Giga drain')
        test_opponent2 = Normal('Eevee', 55, 18, 'Headbut')
        assert test_pokemon.get_multiplier(test_opponent) == 0.5
        assert test_pokemon.get_multiplier(test_opponent1) == 1.5
        assert test_pokemon.get_multiplier(test_opponent2) == 1

    def test_multiplier_function_works_grass(self):
        test_pokemon = Grass('Leafeon', 65, 17, 'Giga drain')
        test_opponent = Fire('Flareon', 65, 20, 'Fire blast')
        test_opponent1 = Water('Vaporeon', 70, 19, 'Hydro pump')
        test_opponent2 = Normal('Eevee', 55, 18, 'Headbut')
        assert test_pokemon.get_multiplier(test_opponent1) == 1.5
        assert test_pokemon.get_multiplier(test_opponent) == 0.5
        assert test_pokemon.get_multiplier(test_opponent2) == 1

    def test_multiplier_function_works_normal(self):
        test_pokemon = Normal('Eevee', 55, 18, 'Headbut')
        test_opponent = Fire('Flareon', 65, 20, 'Fire blast')
        test_opponent1 = Grass('Leafeon', 65, 17, 'Giga drain')
        test_opponent2 = Water('Vaporeon', 70, 19, 'Hydro pump')
        assert test_pokemon.get_multiplier(test_opponent) == 1
        assert test_pokemon.get_multiplier(test_opponent1) == 1
        assert test_pokemon.get_multiplier(test_opponent2) == 1

class TestPokeball:
    def test_pokeball_reuturns_none_if_empty(self):
        test_pokeball = Pokeball()
        assert test_pokeball.stored_pokemon == None
    
    def test_pokeball_returns_caught_pokemon(self):
        Test_pokeball = Pokeball()
        Test_pokeball.catch('Flareon')
        assert Test_pokeball.stored_pokemon == 'Flareon'

    def test_is_empty_returns_true_if_no_pokemon_in_pokeball(self):
        test_pokeball = Pokeball()
        assert test_pokeball.is_empty() == True

    def test_is_empty_return_false_if_pokemon_in_pokeball(self):
        test_pokeball = Pokeball()
        test_pokeball.catch('Flareon')
        assert test_pokeball.is_empty() == False