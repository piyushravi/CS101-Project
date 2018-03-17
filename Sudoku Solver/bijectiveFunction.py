def isValid(constraints):
    '''
    returns if the constraints are valid for bijective function.
    '''

    preImages = {}

    for x in constraints.keys():
        try:
            preImages[constraints[x]] = [False, []]
            return False
        except:
            preImages[constraints[x]] = True

    return [True, preImages]


def bijectiveFunction(constraints, n = 9):
    '''
    returns a bijective mapping on the list of natural
    numbers till n.

    constraints contain a dictionary that specifies what
    values are to be mapped to what numbers.
    '''

    Valid, preImages =  isValid(constraints)
    if Valid:
        res = [0]*n
        lowestUnused = 1
        for x in range(n):
            try:
                res[x] = constraints[x+1]
            except:
                try:
                    while preImages[lowestUnused]:

                        lowestUnused += 1

                except:
                    res[x] = lowestUnused
                    lowestUnused += 1

        return res




    return [0]


if __name__ == "__main__":
    print(bijectiveFunction({}))
