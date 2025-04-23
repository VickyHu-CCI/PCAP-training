
import library.list_utils.lists_utils as lists_utils

def main():
    print("This is the main function of the main module.")
    
    # Example usage of the lists_utils module
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    
    sum_result = lists_utils.sum_elements(my_list)
    print("Sum of elements:", sum_result)
    
    doubled_list = lists_utils.double_each_element(my_list)
    print("Doubled list:", doubled_list)
    
    usage_count = lists_utils.get_usage_counter()
    print("Usage count:", usage_count)

if __name__ == "__main__":
    main()
    print("This is the main module.")
    print("Module name:", __name__)
    print("Module docstring:", __doc__)
    print("Module file:", __file__)
    print("Module package:", __package__)