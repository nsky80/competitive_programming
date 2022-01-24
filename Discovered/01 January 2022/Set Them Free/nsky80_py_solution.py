"""
    Function freeThem() takes "z" (nested list) as parameter and returns the
    free list.
"""
def freeThem(z):
    #initializing empty free list
    # this list contain the free integer numbers
    freeList = []

    # Now checking each element of list and taking appropriate action
    for i in z:

        # if current element 'i' is an integer then add it into freeList
        if type(i) == type(1):
            freeList.append(i)
            
        # else the current element is a list so calling freeThem recursively
        # to free other lists
        else:
            # Here the list 'i' passed to freeThem function which returns a
            # free list so adding the returned list into freeList by using
            # extend function.
            freeList.extend(freeThem(i))

    # returning list of free numbers
    return freeList



# main goes here
if __name__ == "__main__":
    # initializing the list for testing
    x = [1, 2, [3, [4, 5, [6], 7, [8, 9, [[[11, 12]]]]]]]
    print("Given List: ", x)
    
    # calling freeThem function to unpack the list
    print("Free List : ", freeThem(x))
