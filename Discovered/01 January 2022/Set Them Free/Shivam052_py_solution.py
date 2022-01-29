#recursive function
def free(lst):
    freelst = [] # initialize empty list
    for i in lst: # loop to identify the list or other data type
        if type(i) == list:
            freelst.extend(free(i)) # if list call the recursive function
        else:
            freelst.append(i) # append in the free list
    return freelst # return the free list


if __name__ == '__main__':
    #takes the whole nexted list as input
    nexted_lst = eval(input("Enter the whole nexted list: "))
    #print the free list
    print(free(nexted_lst))