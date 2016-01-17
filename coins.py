import itertools

def all_possible_representations(n, dgroup):
    '''
    Returns all possible representations of n using denominations in
    dgroup.
    '''


def brute_force(max_denoms, big_n):
    '''
    Brute force solution to the coin problem.
    '''
    all_dgroups = list(itertools.chain(
        *list(itertools.combinations(
            range(1, big_n+1), num
            ) for num in range(1, max_denoms + 1))
        ))

    # Denomination groups must start with a denomination of 1, otherwise
    # they won't be able to represent the number 1!
    all_dgroups = [dgroup for dgroup in all_dgroups if dgroup[0] == 1]
