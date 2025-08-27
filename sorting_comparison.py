from quicksort import quicksort
from bubblesort import bubblesort, bubblesort_optimized
import time
import random

def test_sorting_algorithms():
    """Test and compare both sorting algorithms"""
    
    # Test with a small array
    test_array = [64, 34, 25, 12, 22, 11, 90, 5]
    print("=== Testing with small array ===")
    print("Original array:", test_array)
    
    # Test QuickSort
    qs_result = quicksort(test_array.copy())
    print("QuickSort result:", qs_result)
    
    # Test BubbleSort
    bs_result = bubblesort(test_array.copy())
    print("BubbleSort result:", bs_result)
    
    # Test with a larger array for performance comparison
    print("\n=== Performance Comparison with Large Array ===")
    large_array = [random.randint(1, 1000) for _ in range(1000)]
    
    # QuickSort timing
    start_time = time.time()
    quicksort(large_array.copy())
    qs_time = time.time() - start_time
    
    # BubbleSort timing
    start_time = time.time()
    bubblesort(large_array.copy())
    bs_time = time.time() - start_time
    
    print(f"QuickSort time for 1000 elements: {qs_time:.6f} seconds")
    print(f"BubbleSort time for 1000 elements: {bs_time:.6f} seconds")
    print(f"QuickSort is {bs_time/qs_time:.1f}x faster than BubbleSort")
    
    # Test with already sorted array
    print("\n=== Testing with Already Sorted Array ===")
    sorted_array = list(range(10))
    print("Already sorted array:", sorted_array)
    
    qs_sorted = quicksort(sorted_array.copy())
    bs_sorted = bubblesort_optimized(sorted_array.copy())
    
    print("QuickSort on sorted array:", qs_sorted)
    print("Optimized BubbleSort on sorted array:", bs_sorted)
    
    # Algorithm characteristics summary
    print("\n=== Algorithm Characteristics Summary ===")
    print("QuickSort:")
    print("- Divide and conquer algorithm")
    print("- Average time complexity: O(n log n)")
    print("- Worst case: O(n²) - when pivot selection is poor")
    print("- In-place but not stable")
    print("- Good for large datasets")
    
    print("\nBubbleSort:")
    print("- Simple comparison-based algorithm")
    print("- Time complexity: O(n²) in worst/average case")
    print("- Best case: O(n) when array is already sorted")
    print("- In-place and stable")
    print("- Good for small datasets or educational purposes")

if __name__ == "__main__":
    test_sorting_algorithms()
