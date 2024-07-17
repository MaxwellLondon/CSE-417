import random as r 

def random_selection(arr, k, comparisons = 0):
    
    #Base case, if the array only has one element you must return 
    if len(arr) == 1:
        return (arr[0], comparisons)

    #Selecting random pivot within the array.
    pivot = r.choice(arr)

    #Array  of all values less than the pivot
    lows = [x for x in arr if x < pivot]
    #Array  of all values greater than the pivot
    highs = [x for x in arr if x > pivot]
    #Array  of all values equal to the pivot
    equals = [x for x in arr if x == pivot]
    # 3 x len(arr) comparisons.
    comparisons += (len(arr) * 3)

    # Calculate which part of the array to recurse on based on the number of
    # elements greater than the pivot.

    if k <= len(highs):
        #Case when K largest is in the high part of array
        return random_selection(highs, k, comparisons)
    elif k <= len(highs) + len(equals):
        #Case when K largest is within the equals part of array
        return (pivot, comparisons)
    else:
        #Case when K largest is in th elow part of the array.

        #K must be adjusted because we are shifting the window of the array to be lower. 

        #If lows is empty, then return pivot. 
        
        if lows:
            return random_selection(lows, k - len(highs) - len(equals), comparisons)
        else:
            return (pivot, comparisons)
        
values = []

for i in range(1, 10):
    for j in range (1, 10):
        arr = [r.randint(1, 500000) for _ in range(i * 500000)]
        k = (i * 500000) / 2
        result = random_selection(arr, k)
        values.append(result[1] / (i*500000))
        print(f"{(i * 500000, result[1])},", end = "")