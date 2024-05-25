def input_array():
    array = []
    n = int(input("Enter the number of elements in the array: "))
    
    print("Enter the elements of the array, separated by spaces:")
    elements = input().split()
    
    for element in elements:
        array.append(int(element))
    
    return array
     
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def replace_elements(arr, target, replacement):
    return [replacement if x == target else x for x in arr]

def main():
    print("Array Sorting and Element Search")
    
    user_array = input_array()
    print("User input array:", user_array)
    
    sorted_array = quick_sort(user_array)
    print("Sorted Array using Quick Sort:", sorted_array)
    
    target = int(input("Enter the element to search for: "))
    
    if target in sorted_array:
        replacement = int(input("Enter the replacement element: "))
        sorted_array = replace_elements(sorted_array, target, replacement)
        print(f"Modified Array after replacing {target} with {replacement}:", sorted_array)
    else:
        print(f"Element {target} not found in the array. No replacement made.")

if __name__ == "__main__":
    main()




