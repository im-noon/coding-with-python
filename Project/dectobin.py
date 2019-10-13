from datastructures.stack import Stack

def dectoBin(decimal):
    s = Stack()
    while decimal > 0:
        rem = decimal % 2
        s.push(rem)
        decimal //= 2

    binString = ''
    while not s.isEmpty():
        binString += str(s.pop())

    return binString;

if __name__ == "__main__":
    print("decimal {} to binary {}".format(42, dectoBin(42)))