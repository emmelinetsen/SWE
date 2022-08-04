# Given a string & array of formats, return the HTML
#
# string = “Hi from me”
# formats = [['b’, 0, 2], [’i’, 3, 7]]
# output = <b>Hi</br> <i>from</i> me
#
# Need to include the nested ones where closing happens before other close
#
# string = “Hello this is very long”
# formats = [['b’, 0, 13], [’i’, 6, 10]]
# output = <b>Hello <i>this <br>is </br></i><br>very long</br></b>

# iterate through the string
# on each position of the string:
# determine whether there is a format that is starting or ending at that position
# if it is a starting position (formats[i][1]), use an open bracket
# if it is an ending position (formats[i][2]), use a closed bracket
# and then add the character at the position of the string

# not the most efficient way because have to iterate through the entire formats array each time
# how to reduce having to iterate through the formats array at each position?
# can use 2 dictionaries -> one for opening, one for closing.
# will do a lookup in the dictionary to see whether there is a format at that position

def stringToHTML(str, formats):
    open_format = addFormatToDict(formats, 1)
    close_format = addFormatToDict(formats, 2)

    html = ""
    for idx, char in enumerate(str):
        if idx in open_format:
            html += "<" + open_format[idx] + ">"
        elif idx in close_format:
            html += "</" + close_format[idx] + ">"
        html += char

    return html


# position -> 1 or 2. determines whether it's for opening or closing format
def addFormatToDict(formats, position):
    d = dict()
    for i in range(len(formats)):
        d[formats[i][position]] = formats[i][0]
    return d

if __name__ == "__main__":
    print(stringToHTML("Hi from me", [['b', 0, 2], ['i', 3, 7]]))
    print(stringToHTML("Hello this is very long", [['b', 0, 13], ['i', 6, 10]]))