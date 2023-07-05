PRIMES = []
def stamp(orderedTokens):
    return [complex(token, PRIMES[i]) for i, token in enumerate(orderedTokens)]


def meld(stampedTokens):
    # todo
    pass