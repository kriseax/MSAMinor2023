import random

def sequential_search(number_list, target_value):
    for index in range(len(number_list)):
        #determin if the number at the current index is equal to target
        #If return the index and end the loop
        if target_value == number_list[index]:
            return index
    
    return -1

"""
Function to run binary search on a sorted list
Inputs: list, target value
Output: found index, or -1
"""
def binary_search(arr, target_value):
    #Define the low and high indexes of the list
    low_index = 0
    high_index = len(arr) - 1

    #Create a loop to search for target value
    while low_index <= high_index:
        #find the middle index
        middle_index = (low_index + high_index) // 2

        #check if target value in at the middle index in the list
        if arr[middle_index] == target_value:
            return middle_index
        elif arr[middle_index] < target_value:
            low_index = middle_index + 1
        else:
            high_index = middle_index - 1

    return -1

def main():
    #create a list of 100 numbers from 1 to 100
    number_list = random.sample(range(1, 101), 100)
    number_list.sort()
    #x = [x for x in range(1, 101)]
    #print(x)

    #found_index = sequential_search(number_list, 105)
    target_value = 65
    found_index = binary_search(number_list, target_value)

    if found_index == -1:
        print(f"{target_value} not found")
    else:
        print(f"{target_value} found at index {found_index}")

main()