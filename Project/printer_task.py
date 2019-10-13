'''
For example, students may print a paper from 1 to 20 pages in length.
If each length from 1 to 20 is equally likely, the actual length for a print
task can be simulated by using a random number between 1 and 20 inclusive.
This means that there is equal chance of any length from 1 to 20 appearing.

If there are 10 students in the lab and each prints twice,
then there are 20 print tasks per hour on average. What is the chance that at
any given second, a print task is going to be created? The way to answer
this is to consider the ratio of tasks to time.
Twenty tasks per hour means that on average there will be one task every 180
seconds:
'''


import random
from datastructures.queue import Queue

class Printer:
    '''
    The Printer class track weather the current task and remaining time
    needed cab be computed from the number of pages in the task.
    '''
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        '''
        Decrement the internal timer and set the printer to idle if task is
        completed.
        :return None
        '''
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        '''
        Validate the current printer task
        :return: the status of Printer task
        '''
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        '''
        Added task to printer and computed amount of time
        :param new task: the next printer task
        :return: None
        '''
        self.currentTask = newtask
        self.timeRemaining = newtask.getPage() * 60 / self.pagerate


class Task:
    '''
    Represent a single printer task
    '''
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randint(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPage(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timestamp

def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

def simulation(timeInsec, ppm):

    printer = Printer(ppm)
    printQueue = Queue()
    waitingTImes = []

    for second in range(timeInsec):
        if newPrintTask():
            task = Task(second)
            printQueue.enqueue(task)

        if (not printer.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingTImes.append(nexttask.waitTime(second))
            printer.startNext(nexttask)

        printer.tick()
    averageWait = sum(waitingTImes)/len(waitingTImes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (
    averageWait, printQueue.size()))

if __name__ == "__main__":
    for i in range(10):
        simulation(3600, 5)