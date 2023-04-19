import random

class Game:
    # Reads file of possible solutions into solution_list.
    with open("answers.txt") as f:
        solution_list = f.read().splitlines()

    def __init__(self):
        self.previous_guesses = list()  # Record of previous guesses for GUI.
        # Record of guessed letters for GUI. [0] = wrong letter; [1] = wrong
        # position; [2] = correct letter.
        self.guessed_letters = dict()
        self.guess_num = 0 # Number of guesses the player has made.
        self.solution = str()   # Correct answer generated at start.
        self.solution_letters = set() # Set of letters in solution to make searching more efficient.
        self.previous_solutions = set()   # Indices of old solutions to avoid repeats.

    def set_solution(self):
        """Sets a new, non-repeat word as the solution.
        """
        while True:   # Generates random solutions until a non-repeated one is found.
            i = random.randint(0, len(self.solution_list) - 1)

            # If the word is a non-repeat, it is set as the solution.
            if i not in self.previous_solutions:
                self.solution = self.solution_list[i]
                self.previous_solutions += i
                break

        # Creates set of characters in solution.
        self.solution_letters = {ch for ch in self.solution}

    def guess(self, guess):
        """Checks user guess and adds letters to guessed letters list, sorted by
        correctness (gren, yellow, grey).

        Args:
            guess (str): Inputted 5 letter guess

        Returns:
            bool: True if correct, false if incorrect.
        """
        guess.lower()
        self.guess_num += 1
        self.previous_guesses.append(guess)

        # Checks if player guessed correctly.
        if guess == self.solution:
            return True

        # If the guess is wrong, each letter is added to the guessed letters list.
        for i in range(5):
            if guess[i] == self.solution[i]: # Correct (green) letters.
                self.guessed_letters[guess[i]] = 2

            elif guess[i] in self.solution_letters: # Wrong position (yellow) letters.
                self.guessed_letters[guess[i]] = 1

            else:   # Wrong (grey) letters.
                self.guessed_letters[guess[i]] = 0

        return False

    def new_game(self):
        """Resets all variables except for previous_solutions to prep for a new game.
        """
        self.previous_guesses = list()
        self.guessed_letters = dict()
        self.solution = str()
        self.solution_letters = set()