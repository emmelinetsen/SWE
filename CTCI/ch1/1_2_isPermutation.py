# Problem 1.2

def is_permutation(str1, str2):
    m = dict()
    for i in str1:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1

    for i in str2:
        if i not in m or m[i] == 0:
            return False
        else:
            m[i] -= 1
    return True

if __name__ == "__main__":
    print(is_permutation("abc", "bcca"))
