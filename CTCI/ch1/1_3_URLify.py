class Solution:
    def URLify(self,string,numChars):
        res= ''
        for i in range(numChars): # O(numChars) where N = numchars
            if string[i] != ' ': # O(current length) <= O(numChars)
                res += string[i]
            elif string[i] == ' ': # O(current length)
                res += "%20"
        return res

    # while space, continue, get ptr2 position. pt1 at the end of the string
    # once there's the first character, move str[ptr1] = str[ptr2], ptr1--, ptr2--
    # when it hits a space,
    # ## str[ptr1] = 0, ptr1--, str[ptr1] = 2, ptr1--, str[ptr1] = %, ptr1--, ptr2--
    def URLify2(self, string, numChars):
        # store the character at the
        arr = [" "] * len(string)
        for i in range(len(string)): # O(length of string)
            arr[i] = string[i]

        ptr1, ptr2 = len(arr) - 1, len(arr) - 1
        while ptr2 >=0: # O(length of string)
            # haven't gone to the first character from the end of the string
            if arr[ptr2] == " " and ptr1 == len(arr) - 1: # O(1)
                ptr2-=1
            elif arr[ptr2] != " ": # O(1)
                arr[ptr1] = arr[ptr2]
                ptr1-=1
                ptr2-=1
            else:
                for i in "02%": # O(length of characters in space)
                    arr[ptr1] = i
                    ptr1-=1
                ptr2-=1
        print(arr[len(string)-numChars-1])
        return "".join(arr) # O (length of string)



if __name__ == '__main__':
    s = Solution()
    print(s.URLify('Mr John Smith    ', 13))
    print(s.URLify2('Mr John  Smith         ', 13))

