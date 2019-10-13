from datastructures.stack import Stack

def decToBase(decimal, base):
    alphanumeric = "0123456789ABCDEF"
    remainders = Stack()
    baseString = ''
    while decimal > 0:
        remainder = decimal % base
        remainders.push(remainder)
        decimal //= base

    while not remainders.isEmpty():
        baseString += alphanumeric[remainders.pop()]

    return baseString

if __name__ == "__main__":
    number = 12345
    base2 = 2
    base8 = 8
    base16 = 16
    print("decimal {} to base {} = {}".format(number, base2, decToBase(
        number, base2)))
    print("decimal {} to base {} = {}".format(number, base8, decToBase(
        number, base8)))
    print("decimal {} to base {} = {}".format(number, base16, decToBase(
        number, base16)))