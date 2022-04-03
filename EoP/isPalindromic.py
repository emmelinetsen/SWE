def is_palindromic(s):
    # Note that s[~i] for i in [0, len(s) - 1] is s[-(i + 1)].
    for i in range(len(s) // 2):
        print(i, " ", s[i], " ", s[~i])
        # print(s[-(i+1)])
    return all(s[i] == s[~i] for i in range(len(s) // 2))


if __name__ == "__main__":
    print(is_palindromic("rateaetar"))
