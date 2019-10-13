# Converting an Integer to a String in Any Base

def toStr(number, base):
    alphaNumeric = "0123456789ABCDEF"
    if number < base:
        return alphaNumeric[number]
    else:
        return toStr(number // base, base) + alphaNumeric[number %base]


print(toStr(1234, 16))