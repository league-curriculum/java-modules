package _01_Sorting_Algorithms;

public class HeapSorter extends Sorter {
    public HeapSorter() {
        type = "Heap";
    }

    /*
     * For further reference:
     * https://en.wikipedia.org/wiki/Heapsort
     */
    
    @Override
    void sort(int[] array, SortingVisualizer display) {
        // 7. create an integer called n and set it equal 
        //    to the length of the array

        
        // 8. make a for loop that starts half way between
        //    0 and n and counts down until it is less than 0.
        //    Inside this for loop, call the heapSort method with n and i
        //        and update the display

        
        // 9. make a for loop that starts at n-1 
        //     and counts down until it is less than 0.

            // 10. inside this loop swap the array elements at 0 and i.

 
            // 11. inside this loop call the heapSort method with i and 0
            //     Update the display

    }
    
    public void heapSort(int[] array, int n, int i, SortingVisualizer display) {
        // 1. create an integer called largest and set it equal to i

        // 2. create an integer called l and set it equal to 2 * i + 1

        // 3. create an integer called r and set it equal to 2 * i + 2

 
        // 4. if l is less than n 
        //    and array element at l is greater than array element at largest
        //    then set largest equal to l

 
        // 5. if r is less than n 
        //    and array element at r is greater than array element at largest
        //    then set largest equal to r

 
        // 6. if largest is not equal to i
        //    then swap the array elements at i and largest.
        //    Also, call the heapSort method with n and largest
    	//    Update the display    
    }

}