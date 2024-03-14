import itertools

def get_value(word, substitution):
    total = 0
    multiplier = 1
    for letter in reversed(word):
        total += multiplier * substitution[letter]
        multiplier *= 10
    return total

def solve_equation(equation):
    # Split equation into left and right parts
    left, right = equation.lower().replace(' ', '').split('=')
    
    # Split words in the left part
    left = left.split('+')
    
    # Create a set of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol))

if __name__ == '__main__':
    solve_equation('SEND + MORE = MONEY')
