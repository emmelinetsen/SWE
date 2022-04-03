def stringCompression(s):
    # assuming that len(s) >= 1
    res = ""
    if compressedLen(s) > len(s):
        return s
    else:
        charCount = 0
        currentChar = s[0]
        values = []
        for i in s:
            if i == currentChar:
                charCount += 1
            else:
                values.append(currentChar)
                values.append(str(charCount))
                currentChar = i
                charCount = 1

    values.append(currentChar)
    values.append(str(charCount))
    res = res.join(values)
    return res

def compressedLen(s):
    # charCount = 0
    currentChar = s[0]
    diff = 1
    for i in s:
        if i != currentChar:
            currentChar = i
            diff += 1

    return diff * 2

if __name__ == '__main__':
    print(stringCompression("a"))
    print(stringCompression("aab"))
    print(stringCompression("aabb"))
    print(stringCompression("aabbb"))
    print(stringCompression("aabcccccaaa"))