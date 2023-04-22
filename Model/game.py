import random

class Game:
    # Reads file of possible solutions into solution_list.
    with open("answers.txt") as f:
        solution_list = f.read().splitlines()

    def __init__(self):
        # Record of guessed letters for GUI. [0] = wrong letter; [1] = wrong
        # position; [2] = correct letter.
        self.guessed_letters = [0, 0, 0, 0, 0]
        self.guess_num = 0 # Number of guesses the player has made.
        self.solution = str()   # Correct answer generated at start.
        self.previous_solutions = set()   # Indices of old solutions to avoid repeats.

    def set_solution(self):
        """Sets a new, non-repeat word as the solution.
        """
        while True:   # Generates random solutions until a non-repeated one is found.
            i = random.randint(0, len(self.solution_list) - 1)

            # If the word is a non-repeat, it is set as the solution.
            if i not in self.previous_solutions:
                self.solution = self.solution_list[i]
                self.previous_solutions.add(i)
                break

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
        self.guessed_letters = [0, 0, 0, 0, 0]

        solution_copy = [ch for ch in self.solution]   # Solution list that can be modified. 

        # Checks if player guessed correctly.
        if guess == self.solution:
            self.guessed_letters = [2, 2, 2, 2, 2]
            return True

        # If the guess is wrong, the color of each letter (represented by an int 0-2) 
        # is added to guessed_letters in the corresponding position.
        for i in range(5):  # Correct (green) letters are checked first.
            if guess[i] == solution_copy[i]: 
                self.guessed_letters[i] = 2
                # Letters are removed from solution_copy as checked to avoid overwriting.
                solution_copy[i] = " "


        for i in range(5):
            if not self.guessed_letters[i]:  # Only checks non-green letters.
                if guess[i] in solution_copy: # Wrong position (yellow) letters.
                    self.guessed_letters[i] = 1
                    j = solution_copy.index(guess[i])  # Removes 1st occurence to account for doubles.
                    solution_copy[j] = " "

                else:   # Wrong (grey) letters.
                    self.guessed_letters[i] = 0

        return False

    def new_game(self):
        """Resets all variables except for previous_solutions to prep for a new game.
        """
        self.guessed_letters = [0, 0, 0, 0, 0]
        self.solution = str()
        self.guess_num = 0