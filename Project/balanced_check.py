from datastructures.stack import Stack

def balanceCheck(symbols):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbols) and balanced:
        symbol = symbols[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matched(top, symbol):
                    balanced =False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matched(open, close):
    opens = "({["
    closers = ")}]"
    return opens.index(open) == closers.index(close)


if __name__ == "__main__":
    print(balanceCheck('{{([][])}()}'))
    print(balanceCheck('[{()]'))