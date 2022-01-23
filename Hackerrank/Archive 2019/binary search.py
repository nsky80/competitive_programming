
def binarySearch(arr, x, low, high):
    while low < high:
        mid = (high + low) // 2
        if arr[mid] == x:
            break
        elif arr[mid] > x:
            high = mid-1
        else:
            low = mid+1
    mid = (high + low) // 2
    if x <= arr[mid]:
        return mid
    else:
        return mid+1


if __name__ == "__main__":
    arr = [2, 4, 6, 23, 34, 43, 56, 58, 88, 98]
    f = binarySearch(arr, 10, 0, 10)
    print(f)