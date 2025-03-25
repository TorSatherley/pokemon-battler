from src.pokemon import (
    Pokemon,
    Fire,
    Water,
    Grass,
    Normal,
    Pokeball,
    Trainer,
    Battle,
    get_pokemon_class,
    pokemon_table,
    get_pokemon_id,
)
import pytest
from unittest.mock import patch


class TestProperties:
    def test_eevee_returns_relevant_properties(self):
        test_pokemon = Pokemon("Eevee", 55, 18, "Headbuttt")
        assert test_pokemon.name == "Eevee"
        assert test_pokemon.hit_points == 55
        assert test_pokemon.attack_damage == 18
        assert test_pokemon.move == "Headbuttt"


class TestMethods:
    def test_use_move_returns_string(self):
        test_pokemon = Pokemon("Eevee", 55, 18, "Headbuttt")
        assert test_pokemon.use_move() == "Eevee used Headbuttt!"

    def test_takes_damage_reduces_health_by_attack_damage(self):
        test_pokemon = Pokemon("Eevee", 55, 18, "Headbuttt")
        test_pokemon.take_damage(20)
        assert test_pokemon.hit_points == 35

    def test_has_fainted_happens_when_health_hits_zero(self):
        test_pokemon = Pokemon("Eevee", 55, 18, "Headbuttt")
        test_pokemon.take_damage(55)
        assert test_pokemon.has_fainted() == True

    def test_has_fainted_happends_when_health_below_zero(self):
        test_pokemon = Pokemon("Eevee", 55, 18, "Headbuttt")
        test_pokemon.take_damage(60)
        assert test_pokemon.has_fainted() == True

    def test_has_fainted_returns_false_when_health_above_zero(self):
        test_pokemon = Pokemon("Eevee", 55, 18, "Headbuttt")
        test_pokemon.take_damage(50)
        assert test_pokemon.has_fainted() == False


class TestTypes:
    def test_fire_type_inherites_from_base_class(self):
        test_pokemon = Fire("Flareon", 65, 20, "Fire blast")
        assert test_pokemon.name == "Flareon"
        assert test_pokemon.hit_points == 65
        assert test_pokemon.attack_damage == 20
        assert test_pokemon.move == "Fire blast"

    def test_Grass_type_inherites_from_base_class(self):
        test_pokemon = Grass("Leafeon", 65, 17, "Giga drain")
        assert test_pokemon.name == "Leafeon"
        assert test_pokemon.hit_points == 65
        assert test_pokemon.attack_damage == 17
        assert test_pokemon.move == "Giga drain"

    def test_water_type_inherites_from_base_class(self):
        test_pokemon = Water("Vaporeon", 70, 19, "Hydro pump")
        assert test_pokemon.name == "Vaporeon"
        assert test_pokemon.hit_points == 70
        assert test_pokemon.attack_damage == 19
        assert test_pokemon.move == "Hydro pump"

    def test_normal_type_inheries_from_base_class(self):
        test_pokemon = Normal("Eevee", 55, 18, "Headbutt")
        assert test_pokemon.name == "Eevee"
        assert test_pokemon.hit_points == 55
        assert test_pokemon.attack_damage == 18
        assert test_pokemon.move == "Headbutt"

    def test_multiplier_function_works_water(self):
        test_pokemon = Water("Vaporeon", 70, 19, "Hydro pump")
        test_opponent = Fire("Flareon", 65, 20, "Fire blast")
        test_opponent1 = Grass("Leafeon", 65, 17, "Giga drain")
        test_opponent2 = Normal("Eevee", 55, 18, "Headbutt")
        assert test_pokemon.get_multiplier(test_opponent) == 1.5
        assert test_pokemon.get_multiplier(test_opponent1) == 0.5
        assert test_pokemon.get_multiplier(test_opponent2) == 1

    def test_multiplier_function_works_fire(self):
        test_pokemon = Fire("Flareon", 65, 20, "Fire blast")
        test_opponent = Water("Vaporeon", 70, 19, "Hydro pump")
        test_opponent1 = Grass("Leafeon", 65, 17, "Giga drain")
        test_opponent2 = Normal("Eevee", 55, 18, "Headbutt")
        assert test_pokemon.get_multiplier(test_opponent) == 0.5
        assert test_pokemon.get_multiplier(test_opponent1) == 1.5
        assert test_pokemon.get_multiplier(test_opponent2) == 1

    def test_multiplier_function_works_grass(self):
        test_pokemon = Grass("Leafeon", 65, 17, "Giga drain")
        test_opponent = Fire("Flareon", 65, 20, "Fire blast")
        test_opponent1 = Water("Vaporeon", 70, 19, "Hydro pump")
        test_opponent2 = Normal("Eevee", 55, 18, "Headbutt")
        assert test_pokemon.get_multiplier(test_opponent1) == 1.5
        assert test_pokemon.get_multiplier(test_opponent) == 0.5
        assert test_pokemon.get_multiplier(test_opponent2) == 1

    def test_multiplier_function_works_normal(self):
        test_pokemon = Normal("Eevee", 55, 18, "Headbutt")
        test_opponent = Fire("Flareon", 65, 20, "Fire blast")
        test_opponent1 = Grass("Leafeon", 65, 17, "Giga drain")
        test_opponent2 = Water("Vaporeon", 70, 19, "Hydro pump")
        assert test_pokemon.get_multiplier(test_opponent) == 1
        assert test_pokemon.get_multiplier(test_opponent1) == 1
        assert test_pokemon.get_multiplier(test_opponent2) == 1


class TestPokeball:
    def test_pokeball_reuturns_none_if_empty(self):
        test_pokeball = Pokeball()
        assert test_pokeball.stored_pokemon == None

    def test_pokeball_returns_caught_pokemon(self):
        # Arrange
        eevee = Normal("Eevee", 55, 18, "Headbutt")
        Test_pokeball = Pokeball()
        # Act
        Test_pokeball.catch(eevee)
        # Assert
        assert Test_pokeball.stored_pokemon == eevee

    def test_is_empty_returns_true_if_no_pokemon_in_pokeball(self):
        test_pokeball = Pokeball()
        assert test_pokeball.is_empty() == True

    def test_is_empty_return_false_if_pokemon_in_pokeball(self):
        flareon = Fire("Flareon", 65, 20, "Fire blast")
        test_pokeball = Pokeball()
        test_pokeball.catch(flareon)
        assert test_pokeball.is_empty() == False


class TestTrainer:
    def test_throw_pokeball_will_allocate_pokemon_to_ball(self):
        # Arrange
        flareon = Fire("Flareon", 65, 20, "Fire blast")
        # Act
        test_throw = Trainer()
        test_throw.throw_pokeball(flareon)
        # Assert
        assert test_throw.trainer_belt[0].stored_pokemon == flareon

    def test_throw_pokeball_will_allocate_multiple_throws(self):
        # Arrange
        flareon = Fire("Flareon", 65, 20, "Fire blast")
        eevee = Normal("Eevee", 55, 18, "Headbutt")
        leafeon = Grass("Leafeon", 65, 17, "Giga drain")
        # Act
        vaporeon = Fire("Vaporeon", 70, 19, "Hydro pump")
        test_throw = Trainer()
        test_throw.throw_pokeball(flareon)
        test_throw.throw_pokeball(eevee)
        test_throw.throw_pokeball(leafeon)
        # Assert
        assert test_throw.trainer_belt[0].stored_pokemon == flareon
        assert test_throw.trainer_belt[1].stored_pokemon == eevee
        assert test_throw.trainer_belt[2].stored_pokemon == leafeon
        assert test_throw.trainer_belt[3].stored_pokemon == None

    def test_throw_pokeball_should_fail_if_no_available_space(self):
        # Arrange
        flareon = Fire("Flareon", 65, 20, "Fire blast")
        eevee = Normal("Eevee", 55, 18, "Headbutt")
        leafeon = Grass("Leafeon", 65, 17, "Giga drain")
        vaporeon = Fire("Vaporeon", 70, 19, "Hydro pump")
        charmander = Fire("Charmander", 44, 17, "Flamethrower")
        squirtle = Water("Squirtle", 44, 16, "Surf")
        bulbasaur = Grass("Bulbasaur", 45, 16, "Razor leaf")
        # Act
        test_throw = Trainer()
        test_throw.throw_pokeball(flareon)
        test_throw.throw_pokeball(eevee)
        test_throw.throw_pokeball(leafeon)
        test_throw.throw_pokeball(vaporeon)
        test_throw.throw_pokeball(charmander)
        test_throw.throw_pokeball(squirtle)
        # Assert
        assert test_throw.throw_pokeball(bulbasaur) == "Belt is full!"


class TestBattle:
    def test_battle_initialises_two_pokemon_objects(self):
        flareon = Fire("Flareon", 65, 20, "Fire blast")
        squirtle = Water("Squirtle", 44, 16, "Surf")
        # Act
        test_battle = Battle(flareon, squirtle)
        # Assert
        assert test_battle.pokemon_1 == flareon
        assert test_battle.pokemon_2 == squirtle

    def test_battle_hit_points_decreased_by_attack_damage_with_multiplier(self):
        flareon = Fire("Flareon", 65, 20, "Fire blast")
        squirtle = Water("Squirtle", 44, 16, "Surf")

        test_battle = Battle(flareon, squirtle)
        test_battle.take_turn()

        assert test_battle.pokemon_2.hit_points == 34

    def test_that_turn_counter_changes_with_turns_taken(self):
        flareon = Fire("Flareon", 65, 20, "Fire blast")
        squirtle = Water("Squirtle", 44, 16, "Surf")

        test_battle = Battle(flareon, squirtle)

        assert test_battle.turn_counter == 1
        test_battle.take_turn()
        assert test_battle.turn_counter == 2
        test_battle.take_turn()
        assert test_battle.turn_counter == 1
        test_battle.take_turn()
        assert test_battle.turn_counter == 2

    def test_get_winner_declares_winner(self):
        flareon = Fire("Flareon", 65, 20, "Fire blast")
        squirtle = Water("Squirtle", 44, 16, "Surf")

        test_battle = Battle(flareon, squirtle)

        test_battle.take_turn()
        assert test_battle.pokemon_2.hit_points == 34
        assert test_battle.get_winner(flareon, squirtle) == None

        test_battle.take_turn()
        assert test_battle.pokemon_1.hit_points == 41
        assert test_battle.get_winner(squirtle, flareon) == None

        test_battle.take_turn()
        assert test_battle.pokemon_2.hit_points == 24
        assert test_battle.get_winner(flareon, squirtle) == None

        test_battle.take_turn()
        assert test_battle.pokemon_1.hit_points == 17
        assert test_battle.get_winner(squirtle, flareon) == None

        winner = test_battle.take_turn()
        assert test_battle.pokemon_2.hit_points == 14
        assert test_battle.get_winner(flareon, squirtle) == None
        assert winner == None

        winner = test_battle.take_turn()
        assert test_battle.pokemon_1.hit_points == -7
        assert (
            test_battle.get_winner(squirtle, flareon)
            == "Flareon has fainted! Squirtle has won!"
        )
        assert winner == "Flareon has fainted! Squirtle has won!"

    def test_take_turn_raises_exception_for_already_fainted_pokemon(self):
        flareon = Fire("Flareon", 65, 20, "Fire blast")
        squirtle = Water("Squirtle", 44, 16, "Surf")

        test_battle = Battle(flareon, squirtle)

        test_battle.take_turn()
        test_battle.take_turn()
        test_battle.take_turn()
        test_battle.take_turn()
        test_battle.take_turn()

        winner = test_battle.take_turn()
        assert test_battle.pokemon_1.hit_points == -7
        assert (
            test_battle.get_winner(squirtle, flareon)
            == "Flareon has fainted! Squirtle has won!"
        )
        assert winner == "Flareon has fainted! Squirtle has won!"

        message = test_battle.take_turn()
        assert message == "Flareon has fainted! Squirtle has won!"


@pytest.fixture
def pokemon_test_table():
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


class TestGetPokemonClass:
    def test_function_returns_normal_type_for_normal_input(self, pokemon_test_table):
        pokemon_data, _ = pokemon_test_table
        choice_num = 1
        result = get_pokemon_class(pokemon_data, choice_num)
        assert result.type == "Normal"
        assert result.name == "Eevee"
        assert result.hit_points == 55
        assert result.move == "Headbutt"
        assert result.attack_damage == 18

    def test_function_returns_fire_type_for_fire_input(self, pokemon_test_table):
        pokemon_data, _ = pokemon_test_table
        choice_num = 2
        result = get_pokemon_class(pokemon_data, choice_num)
        assert result.type == "Fire"
        assert result.name == "Flareon"
        assert result.hit_points == 65
        assert result.move == "Fire blast"
        assert result.attack_damage == 20

    def test_function_returns_water_type_for_water_input(self, pokemon_test_table):
        pokemon_data, _ = pokemon_test_table
        choice_num = 3
        result = get_pokemon_class(pokemon_data, choice_num)
        assert result.type == "Water"
        assert result.name == "Vaporeon"

    def test_function_returns_grass_type_for_grass_input(self, pokemon_test_table):
        pokemon_data, _ = pokemon_test_table
        choice_num = 7
        result = get_pokemon_class(pokemon_data, choice_num)
        assert result.type == "Grass"
        assert result.name == "Bulbasaur"


class TestGetPokemonID:
    def test_function_returns_id_for_valid_input(self):
        with patch("builtins.input", side_effect=[4]):
            result = get_pokemon_id("Tor")
            assert result == 4

    def test_manages_invalid_id(self, capsys):
        with patch("builtins.input", side_effect=[10, 0, 3]):
            result = get_pokemon_id("Tor")
            captured = capsys.readouterr()
            assert (
                captured.out
                == "10 is not a valid Pokemon ID.\n0 is not a valid Pokemon ID.\n"
            )
            assert result == 3
