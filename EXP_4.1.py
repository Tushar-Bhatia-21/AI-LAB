from itertools import permutations

def solve_cryptarithmetic(puzzle):
    # Extracting unique letters from the puzzle
    letters = set(puzzle.replace(' ', ''))

    # Generating permutations of digits from 0 to 9
    digit_permutations = permutations(range(10), len(letters))

    for perm in digit_permutations:
        # Mapping letters to digits
        digit_mapping = {letter: digit for letter, digit in zip(letters, perm)}
        
        # Replace letters with corresponding digits and evaluate the expression
        expression = ''.join(str(digit_mapping.get(letter, letter)) for letter in puzzle)
        expression = expression.replace(' ', '')  # Remove spaces
        if eval(expression):
            return digit_mapping

    return None

# User input for the cryptarithmetic puzzle
puzzle = input("Enter the cryptarithmetic puzzle: ")

solution = solve_cryptarithmetic(puzzle)
if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")
