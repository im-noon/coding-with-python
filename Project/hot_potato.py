from datastructures.queue import Queue

def hotPotato(names, num):
    simQueue = Queue()
    for name in names:
        simQueue.enqueue(name)

    while simQueue.size() > 1:
        for i in range(num):
            simQueue.enqueue(simQueue.dequeue())

        simQueue.dequeue()
    return simQueue.dequeue()

if __name__ == "__main__":
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))