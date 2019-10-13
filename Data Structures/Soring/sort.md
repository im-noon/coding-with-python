Sorting algorithm
-
* A sorting algorithm is an algorithm that puuts elements of and array in a certain order.
* Numbers ->  numerical ordering!!!
* Strings, characters 0-> alphabetical ordering!!!

#### Type of sorting algorithm:

* Comparision base algorithm: compare the item
    - > bubble sort, insertion sort, selection sort, merge sort, quick sort
* Non-comparision based sorting: not compare the iem
    - > radix sort, bucket sort
    
#### Features:
* Time complexity: O(N<sup>2</sup>) or O(N logN) or O(N)
* In place: strictly an in-place sort needs only O(1) memory beyond the items being sorted,
 so an in-place algorithm does nit need any extra memory.
    - quick sort
* Recursive: some sorting algorithms are implemented in a recursive manner
    - > the divide and conquer ones especially.
    // merge sort and quick sort
* Stable: stable sorting algorithms maintain the relative order of the records with equal values.
    - > merge sort

#### Adaptive sorting:
 * An adaptive algorithm is an algorithm that changes its behaviors based on information available at runtime.
 * Adaptive sort takes advantage of existing order in its input.
 * It benefits from local orders 
    - > sometimes an unsorted array contains sequences that are sorted by default.
    - > the algorithm will sort faster.
 * Most of the times: we jsut have to modify existing sorting algorithms in order to end up with an adaptive one.
 * Comparison based algorithms have optimal O(N logN) running time complexity.
 * Adaptive sort takes advantage of the existing order of the input to try to achieve better times: maybe O(N) could be reached.
 * The more presorted the input is, the faster it should be sorted.
 * IMPORTANT:nearly sorted sequences are common in practice!!!
 * Heap sort, merge sort: not adaptive algorithms, do not take advantage of presorted sequences.
 * Shell sort: adaptive algorithm so perform better if the input is partially sorted.
 