from __future__ import print_function
import time
import copy
import random

def naivesort (unsorted):
    if (len(unsorted) <= 1):
        return unsorted

    i = len(unsorted)
    result = []
    while i > 0:
        lowest = unsorted[0]
        for j in range(1,len(unsorted)):
            if (unsorted[j] < lowest):
                lowest = unsorted[j]
        result.append(lowest)
        unsorted.remove(lowest)
        i -= 1
    return result

def mergesort (unsorted):
	# unsorted: a list of unsorted elements

    # base case
    if (len(unsorted) <= 1):
        return unsorted

    # divide the list in 2 equally sized lists
    middle = len(unsorted)/2
    l = unsorted[:middle]
    r = unsorted[middle:]

    # conquer: call mergesort for left and right
    left = mergesort(l)
    right = mergesort(r)

    # combine
    result = []
    nl = len(left)
    nr = len(right)
    i = j = 0
    while (i < nl and j < nr):
        if (left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # append any items remaining in the right or the left list
    if (i < nl):
        result += left[i:]
    elif (j < nr):
        result += right[j:]

    return result    

def QS_Swap(array, e1, e2):
    if e1 == e2:
        return

    tmp = array[e1]
    array[e1] = array[e2]
    array[e2] = tmp

def quicksort(unsorted, begin=0, end=None):
    # this is an in-place implementation. Array is not returned,
    # but is altered in the recursive algorithm
    if end == None:
        end = len(unsorted)-1

    # base case
    if begin >= end:
        return

    p_i = random.randint(begin, end)
    QS_Swap(unsorted, begin, p_i)      # place pivot at the front
    p = unsorted[begin]

    # partition the list in elements <p and elements >=p
    # invariant:
    #    i is the left-most element of the elements >=p
    #    j is the left-most element of the unpartioned elements
    i = begin+1
    for j in range(i, end+1):
        if unsorted[j] < p:
            QS_Swap(unsorted,j,i)
            i += 1
    #endfor: j==end

    QS_Swap(unsorted, begin,i-1) # swap pivot & right-most element <p
    p_i = i-1      # p_i >= begin

    # recursive call to quicksort for elements <p and >=p excluding p
    # left=[0:p_i] right=[p_i+1,n]
    quicksort(unsorted, begin, p_i-1)
    quicksort(unsorted, p_i, end)

def test():
    assert(mergesort([5,3,6,7,1,9,2,8,4]) == [1,2,3,4,5,6,7,8,9])
    assert(mergesort([])) == []
    assert(mergesort([2])) == [2] 

    assert(naivesort([5,3,6,7,1,9,2,8,4]) == [1,2,3,4,5,6,7,8,9])
    assert(naivesort([])) == []
    assert(naivesort([2])) == [2] 

test()

data=[5,3,6,7,1,9,2,8,4] # for testing

filename = 'QuickSort.txt'
with open(filename) as f_obj:
    contents = f_obj.readlines()
    data = [int(val) for val in contents]
#print(data)
#print(data[0])

start = time.time()
#print("data=", data)
#print("result=",naivesort(copy.copy(data)))
naivesort(copy.copy(data))
print ("naivesort took", time.time() - start, "s, n=", len(data))

start = time.time()
#print("data=", data)
#print("result=",mergesort(copy.copy(data)))
mergesort(copy.copy(data))
print ("mergesort took", time.time() - start, "s, n=", len(data))

start = time.time()
#print("data=", data)
print("result=",quicksort(copy.copy(data)))
#quicksort(copy.copy(data))
print ("quicksort took", time.time() - start, "s, n=", len(data))
