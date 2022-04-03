def oneAway(string1, string2):

    if abs(len(string1) - len(string2)) > 1:
        return False

    a, b = 0, 0
    one = 0
    while a < len(string1) and b < len(string2): # O(length of shorter string)
        if string1[a] != string2[b]:
            if one == 1:
                return False
            one += 1
            if len(string1) > len(string2):
                a += 1
            elif len(string1) < len(string2):
                b += 1
            elif len(string1) == len(string2):
                a+=1
                b+=1
        else:
            a+=1
            b+=1

    if a == len(string1) and b == len(string2):
        return True
    else:
        if one == 0:
            return True
        return False
    return True
    # one extra character at the end of the string and the rest of the string is the same
    # if abs(len(string1) - len(string2)) == 1:

def oneEditInsert(string1, string2):
    idx1=0
    idx2=0
    while idx2 < len(string2) and idx1 < len(string1):
        if string1[idx1] != string2[idx2]:
            if idx1 != idx2:
                return False
            idx2+=1
        else:
            idx1+=1
            idx2+=1
    return True


if __name__ == "__main__":
    print (oneAway("pales", "bakes"))
    print (oneAway("pale", "ple"))
    print (oneAway("pales", "pale"))
    print (oneAway("pale", "bale"))

    print (oneEditInsert("al", "kal"))