def bubblesort(arr):
    """
    BubbleSort Algorithm Implementation
    
    BubbleSort is a simple comparison-based sorting algorithm that works by:
    1. Repeatedly stepping through the list
    2. Comparing adjacent elements and swapping them if they are in the wrong order
    3. The pass through the list is repeated until no swaps are needed
    
    Time Complexity: 
    - Best case: O(n) - when array is already sorted
    - Average/Worst case: O(n²)
    
    Space Complexity: O(1) - only requires a constant amount of additional space
    
    Characteristics:
    - In-place sorting (modifies the original array)
    - Stable sort (preserves relative order of equal elements)
    - Simple to understand and implement
    - Inefficient for large datasets
    """
    
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize - if no swapping occurs, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped in inner loop, then array is sorted
        if not swapped:
            break
    
    return arr


def bubblesort_optimized(arr):
    """
    Optimized version of BubbleSort with early termination
    This version stops early if the array becomes sorted
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        # Reduce the range by i each iteration since the last i elements are sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Early termination if no swaps occurred
        if not swapped:
            break
    
    return arr


# Example usage and testing
if __name__ == "__main__":
    # Test the bubblesort algorithm
    test_array = [64, 34, 25, 12, 22, 11, 90, 5]
    print("Original array:", test_array)
    
    sorted_array = bubblesort(test_array.copy())
    print("BubbleSorted array:", sorted_array)
    
    # Test optimized version
    test_array2 = [1, 2, 3, 4, 5]  # Already sorted
    print("\nTesting optimized version on already sorted array:", test_array2)
    optimized_sorted = bubblesort_optimized(test_array2.copy())
    print("Optimized BubbleSort result:", optimized_sorted)
    
    # Algorithm comparison
    print("\n--- BubbleSort Characteristics ---")
    print("BubbleSort Advantages:")
    print("- Simple to understand and implement")
    print("- Stable sorting algorithm")
    print("- In-place sorting with O(1) space complexity")
    print("- Good for small datasets or nearly sorted arrays")
    
    print("\nBubbleSort Disadvantages:")
    print("- Very slow for large datasets (O(n²) time complexity)")
    print("- Poor cache performance")
    print("- Many unnecessary comparisons even in best case")
    
    print("\n--- When to use BubbleSort ---")
    print("- Educational purposes (teaching sorting concepts)")
    print("- Very small datasets (n < 10)")
    print("- When simplicity is more important than performance")
    print("- When stability is required and dataset is small")
