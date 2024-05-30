package _01_Sorting_Algorithms;

public class MergeSorter extends Sorter {
    public MergeSorter() {
        type = "Merge";
    }

    /*
     * For further reference:
     * https://en.wikipedia.org/wiki/Merge_sort
     */
    
    @Override
    void sort(int[] array, SortingVisualizer display) {
        // 20. call the mergeSort method with 0 and the length of the array minus one

    }
    
    private void mergeSort(int[] array, int low, int high, SortingVisualizer display) {
        // 1. Create a temporary integer array that is the same length as the passed in array.

        
        // 2. make an if statement that checks if low is less than high
        //    and put the rest of the method inside of it

            // 3. Create an integer called middle and set it 
            //    equal to the half way point between low and high

            
            // 4. call the mergeSort method with low and middle

            // 5. call the mergeSort method with middle + 1 and high

            
            // 6. copy the elements from the array into the temporary array,
            //    but only the elements from low to high inclusive

            
            // 7. create three integers called i, j, and k and
            //    set them equal to low, middle + 1, and low respectively

            
            // 8. while i is less than or equal to middle
            //    and j is less than or equal to high
        	//  (ends after step 15)

                // 9. if temp array at i is less than or equal 
                //    to temp array at j 

                    // 10. set array at k equal to temp array at i

                    // 11. increase i by 1

                // 12. else (ends after step 14)

                    // 13. set array at k equal to temp array at j

                    // 14. increase j by 1


                // 15. increase k by 1 and update the display



            // 16. make a while loop that runs while i is less than or equal to middle

                // 17. set array at k equal to temp array at i

                // 18. increase k and i by 1 and update the display


    }

}