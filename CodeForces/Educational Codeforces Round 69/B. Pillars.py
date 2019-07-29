"""
inputCopy
4
1 3 4 2
outputCopy
YES
inputCopy
3
3 1 2
outputCopy
NO

https://codeforces.com/contest/1197/problem/B

    while disk:
        n = len(disk)
        if 0 < ind < n - 1:  # both left and right are present
            if disk[ind-1] > disk[ind+1] and disk[ind-1] < disk[ind]:   # if left element popped out
                temp = disk.pop(ind-1)
                ind -= 1
                disk[ind] = temp
            elif disk[ind] > disk[ind+1]:                   # if right element popped out
                temp = disk.pop(ind+1)
                disk[ind] = temp
            else:
                break
        elif ind > 0 and disk[ind] > disk[ind-1]:    # only left
            temp = disk.pop(ind-1)
            ind -= 1
            disk[ind] = temp
        elif ind < n - 1 and disk[ind] > disk[ind+1]:
            disk.pop(ind)
        else:
            break

    if len(disk) == 1:
        return "YES"
    else:
        return "NO"

"""
def oprations(arr, fix, cur, flag):
    temp = arr[cur]
    arr[cur] = -1
    if flag == 1:
        cur -= 1
    else:
        cur += 1
    arr[fix] = temp
    return cur


def pillars(n, disk):
    # first find the index of max element
    ind = max(range(len(disk)), key=disk.__getitem__)
    left = ind - 1
    right = ind + 1
    l_n = n - 1
    while left >= 0 or right <= n - 1 and l_n > 0:
        if 0 <= left and right <= n - 1:  # both left and right are present
            if disk[right] < disk[left] < disk[ind]:   # if left element popped out
                left = oprations(disk, ind, left, 1)
                l_n -= 1
            elif disk[ind] > disk[right]:                   # if right element popped out
                right = oprations(disk, ind, right, 2)
                l_n -= 1
            else:
                break
        elif left >= 0 and disk[ind] > disk[left]:    # only left
            left = oprations(disk, ind, left, 1)
            l_n -= 1
        elif right <= n - 1 and disk[ind] > disk[right]:
            right = oprations(disk, ind, left, 2)
            l_n -= 1
        else:
            break

    if not l_n:
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    n = int(input())
    disk = list(map(int, input().strip().split()))
    print(pillars(n, disk))