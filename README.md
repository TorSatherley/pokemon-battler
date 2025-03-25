# Pokemon Battler

## Intro

This project is a simple, command-line operated Pokemon Battler game designed to pit two Pokemons against each other.

The game allows players to:

- Choose their trainer name
- Choose their Pokemon to do battle
- Watch the battle unfold, and see who is the victor

All through interfacing with the command line of their terminal.

## About

The main purpose of this project has been for the author (Tor Satherley) to demonstrate some of his OOP (Object Oriented Programming) skills, as well as his ability to write high quality unit tests. The main skills demonstrated include:

- Class composition
- Extending a class from a parent class
- Quality test driven development

## Prerequisites

Before setting up and playing this Pokemon Battler game, ensure you have the following installed and configured:

- Python 3.13 (recommended latest stable version)

    Check if Python is installed: 
```bash
  python --version
```

If not installed, download it from [python.org](https://www.python.org/downloads/).

- pip (Python package manager)

    Check if pip is installed: 
```bash
  pip --version
```

If missing, install it:
```bash
  python -m ensurepip --default-pip
```

## Run Locally

Fork the repo from https://github.com/TorSatherley/pokemon-battler

Clone the project:

```bash
  git clone https://github.com/TorSatherley/pokemon-battler
```

Go to the project directory:

```bash
  cd pokemon-battler
```

Create a new Virtual Environment (recommended):

```bash
  python -m venv venv
```

Activate venv:
```bash
  source venv/bin/activate  # On Linux/macOS
  venv\Scripts\activate  # On Windows
```

Install dependencies

```bash
  pip install -r requirements.txt
```

To test the Pokemon Battler game, from the root of the repository run:

```bash
  export PYTHONPATH=$(pwd)
```
to allow Python to access all files in this repository, then run:

```bash
  pytest
```

to ensure all tests are passing and the game is behaving as it should do.

### Playing the Game

In the root of the repo, run:

```bash
  python src/pokemon.py
```

to start the game in the command line. Follow the instruction printed to the terminal to play the game. When the game has finished, run the above command in your terminal to play again!

## Roadmap

There are several improvements and additions that will be added to this game in the future, namely:

- Battles to continue untill all of a trainers Pokeballs in their belt contain unconscious Pokemon
- Implement a critical hit that randomly awards Pokemon triple damage
- Trainer can use a turn to change Pokemon mid-battle
- Pokemon each have a selection of moves that modify attack damage but also consumes power points

## Author

Tor Satherley