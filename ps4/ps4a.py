# Problem Set 4A
# Name: Vincent Thurman
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return sequence
    
    else:
        perms = []
        last_letter = sequence[-1]
        sequence = sequence[:-1]
        prev_perm_list = get_permutations(sequence)
        
        for p in prev_perm_list:
            for pos in range(0,len(p)+1):
                new_p = p[:pos] + last_letter + p[pos:]
                perms.append(new_p)
                
        return list(set(perms))

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'ab'
    print('Input:', example_input)
    print('Expected Output:', ['ba', 'ab'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'abb'
    print('Input:', example_input)
    print('Expected Output:', ['bab', 'abb', 'bba'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'aaa'
    print('Input:', example_input)
    print('Expected Output:', ['aaa'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'vin'
    print('Input:', example_input)
    print('Output:', get_permutations(example_input))
    print(len(get_permutations(example_input)))
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)