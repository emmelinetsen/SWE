def isPalindromePermutation(string):
    m = dict()
    space = 0
    for ch in string: # O(N)
        # if the character is in the map
        if ch.lower() in m:
            m[ch.lower()] += 1
        else:
            if ch.lower() == ' ':
                space += 1
            else:
                m[ch.lower()] = 1

    # evaluate each value in the map
    # if there are an even # of characters in the string, all values must be even
    # if there are an odd # of characters in the string, one value can be == 1, rest need to be even
    # where there is a value that == 1, set a boolean value to true
    odd = False
    strLen = len(string) - space
    print (m.keys(), m.values())
    for values in m.values(): # O(N)
        # if even # of characters in the string
        if strLen % 2 == 0 and values % 2 != 0:
            return False
        # if odd # and there is a value that == 1
        if values == 1:
            if odd:
                return False
            else:
                odd = True
    if strLen % 2 != 0 and odd is False:
        return False
    return True

if __name__ == "__main__":
    print (isPalindromePermutation("Taat"))
