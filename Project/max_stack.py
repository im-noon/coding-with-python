"""
The aim is to design an algorithm that can return the maximum item of a stack
in O(1) running time complexity. We can use O(N) extra memory!

Hint: we can use another stack to track the max item
"""
class MaxStack(object):

    def __init__(self):
        self.main_stack = []
        self.max_stack = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    # adding item
    def push(self, data):
        self.size += 1
        self.main_stack.append(data)
        if self.size == 1:
            self.max_stack.append(data)

        # if the item is largest insert it to max stack, otherwise duplicate
        # top of max stack
        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if self.is_empty():
            return None
        self.size -= 1
        self.max_stack.pop()
        return self.main_stack.pop()

    def get_max(self):
        return self.max_stack[-1]


if __name__ == "__main__":
    max_stack = MaxStack()
    max_stack.push(10)
    max_stack.push(5)
    max_stack.push(1)
    max_stack.push(120)
    max_stack.push(100)


    print("max :{}".format(max_stack.get_max()))