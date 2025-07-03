
"""
numbers = [11,22,33,44,55,66,77,88,99]

key_value = 88

for i in numbers:
    if numbers[i] == key_value:
        found=True
        break
if found is True:
    print(f"Element {key_value} was found")
else:
    print(f"Element {key_value} was not found")
 """



def binary_search(numbers,key_value):
    start_index = 0
    end_index = len(numbers)-1


    while start_index <= end_index:
        mid = (start_index + end_index)//2
        mid_val = numbers[mid]

        if mid_val == key_value:
            return mid
        elif mid_val<key_value:
            start_index = mid_val + 1
        else:
            end_index = mid_val - 1

    return -1

def recursive_binary_search(arr,target,start_index,end_index):
    if start_index > end_index:
        return -1
    mid = (start_index + end_index)//2
    mid_val = arr[mid]
    if mid_val == target:
        return mid
    elif mid_val<target:
        return recursive_binary_search(arr, target, mid + 1, end_index)
    else:
        return recursive_binary_search(arr, target, start_index, mid - 1)



if __name__ == "__main__":
    key_value = 88

    numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    index = binary_search(numbers=numbers,key_value=key_value)

    print(f"Element {key_value} was found at position : {index}")
else:
    print("Element was not found")
