

def bin_search(arr, start, last, chub,times):
    times=times+1 
    if last >= start:
 
        mid = (last + start) // 2
        print("mid->",mid)
 
        #in the middle
        if arr[mid] == chub:
            return times
 
        # can be in left
        elif arr[mid] > chub:
            return bin_search(arr, start, mid - 1, chub,times)
 
        # can be right
        else:
            return bin_search(arr, mid + 1, last, chub,times)
 
    else:
        # nopsies
        return -1
 
# Test array
arr = [ 2, 3, 4,6,10,20,56,67,400 ]
x = 4
time=0 

# Function call
result = bin_search(arr, 0, len(arr)-1, x,time)
 
if result != -1:
    print("found it YOU CHUBSTER!!!", str(result))
else:
    print("oopsies -- find somewhere else")
