def quicksort(arr):
    """
    QuickSort Algorithm Implementation
    
    QuickSort is a divide-and-conquer algorithm that works by:
    1. Selecting a 'pivot' element from the array
    2. Partitioning the array around the pivot (elements < pivot go left, elements > pivot go right)
    3. Recursively applying the same process to the left and right sub-arrays
    
    Time Complexity: 
    - Best/Average case: O(n log n)
    - Worst case: O(n²) - when pivot is always the smallest or largest element
    
    Space Complexity: O(log n) - due to recursion stack
    
    Characteristics:
    - In-place sorting (modifies the original array)
    - Unstable sort (may change relative order of equal elements)
    - Efficient for large datasets
    """
    
    def _quicksort(arr, low, high):
        if low < high:
            # Partition the array and get the pivot index
            pivot_index = partition(arr, low, high)
            
            # Recursively sort elements before and after partition
            _quicksort(arr, low, pivot_index - 1)
            _quicksort(arr, pivot_index + 1, high)
    
    def partition(arr, low, high):
        """
        Partition function that places the pivot element in its correct position
        and arranges all smaller elements to the left and larger to the right
        """
        # Choose the rightmost element as pivot
        pivot = arr[high]
        
        # Index of smaller element (indicates right position of pivot)
        i = low - 1
        
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                i += 1
                # Swap arr[i] and arr[j]
                arr[i], arr[j] = arr[j], arr[i]
        
        # Place pivot in correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # Start the sorting process
    _quicksort(arr, 0, len(arr) - 1)
    return arr


# Example usage and testing
if __name__ == "__main__":
    # Test the quicksort algorithm
    test_array = [64, 34, 25, 12, 22, 11, 90, 5]
    print("Original array:", test_array)
    
    sorted_array = quicksort(test_array.copy())
    print("QuickSorted array:", sorted_array)
    
    # Performance comparison with BubbleSort
    print("\n--- QuickSort vs BubbleSort Comparison ---")
    print("QuickSort Advantages:")
    print("- Much faster for large datasets (O(n log n) vs O(n²))")
    print("- More cache-efficient due to good locality of reference")
    print("- In-place sorting with low memory overhead")
    
    print("\nQuickSort Disadvantages:")
    print("- Worst-case performance can be O(n²)")
    print("- Not stable (may change order of equal elements)")
    print("- Recursive implementation can cause stack overflow for very large arrays")
