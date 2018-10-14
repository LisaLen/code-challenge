'''Write a recursive function for generating all permutations of an input string. Return them as a set.


'''

def get_permutations(my_str):
    if len(my_str) <= 1:
        return set([my_str])



    permutations_without_last_char = get_permutations(my_str[:-1])
    print(permutations_without_last_char)
    last_char = my_str[-1]
    permutations = set()
    for permutation_without_last_char in permutations_without_last_char:
        for i in range(len(permutation_without_last_char)+1):
            permutation = (permutation_without_last_char[:i] + last_char +
                permutation_without_last_char[i:])

            permutations.add(permutation)

    return permutations

print(get_permutations('cats'))
