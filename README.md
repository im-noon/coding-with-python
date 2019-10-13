## Algorithms-and-Data-Structures

* Algorithm analysis is an implementation-independent way of measuring an algorithm.
* Big-O notation allows algorithms to be classified by their dominant process with respect to the size of the problem.


### The Three Laws of Recursion
* A recursive algorithm must have a base case
* A recursive algorithm must change its state and move to ward the base case.
* A recursive algorithm must call itself recursively.

### What is a Stack?
A stack is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. 
This end is commonly referred to as the _**top**_.
The end opposite the top is known as the _**base**_.

The base of the stack is significant since items stored in the stack that are closer to the base represent those that have been in the stack the longest. 
The most recently added item is the one that is in position to be removed first.
This ordering principle is sometimes called _**LIFO, last-in first-out**_. 

### What Is a Queue?
A queue is an ordered collection of items where the addition of new items happens at one end, called the _*rear*_, 
and the removal of existing items occurs at the other end, commonly called the _*front*_.
As an element enters the queue it starts at the rear and makes its way toward the front, waiting until that time when it is the next element to be removed.
This ordering principle is sometimes called _**FIFO, first-in first-out**_.

### Linked Lists
A linked list is a linear data structure where each element is a separate object. 
Linked list elements are not stored at contiguous location, the elements are linked using pointers. 
Each node of a list is made up of two items - the data and a reference to the next node. 
The last node has a reference to _**null**_.