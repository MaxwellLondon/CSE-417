def weightedIndependentSet(graphArray):
    N = len(graphArray)
    solutionArray = [0] * N
    
    if N == 0:
        return []
   
    if N == 1:
        return [graphArray[0]]

    solutionArray[0] = graphArray[0]
    solutionArray[1] = max(graphArray[0], graphArray[1])
    
    for i in range(2, N):
        solutionArray[i] = max(solutionArray[i-1], solutionArray[i-2]+graphArray[i])
    

    #backtrack to find answers 
    result = []
    i = N-1
    while i >= 0:
        if i == 0:
            result.append(graphArray[i])
            break
        elif i == 1 or solutionArray[i-2]+graphArray[i] < solutionArray[i-1]:
            i -= 1
        else:
            result.append(graphArray[i])
            i -= 2
    
    result.reverse()
    return result

# test_cases = [
#     [1, 2, 3, 4, 5],  # Expected output: [5, 3, 1]
#     [10, 20, 15, 5, 25],  # Expected output: [25, 15, 10]
#     [7, 6, 5, 4, 3, 2, 1],  # Expected output: [7, 5, 3, 1]
#     [3, 2, 1, 5, 4],  # Expected output: [5, 3]
#     [10, 5, 20, 15, 25]  # Expected output: [25, 20, 10]
# ]

# for i, arr in enumerate(test_cases):
#     result = weightedIndependentSet(arr)
#     print(f"Test case {i+1}: Input = {arr}; Output = {result}")


def taskChoice(highStressPayoff, lowStressPayoff):
    N = len(highStressPayoff)

    tasks = [0] * (N + 1)

    tasks[0] = 0

    tasks[1] = highStressPayoff[0]

    for i in range(2, N + 1):
        tasks[i] = max(tasks[i - 2] + highStressPayoff[i - 1], tasks[i - 1] + lowStressPayoff[i - 1])

    
        
    return tasks[N]

# high = [3, 6, 8, 7, 6]
# low = [1, 5, 4, 5, 3]

# print(taskChoice(high, low))


def binaryTreeCounter(K):
    counter = [0] * (K + 1)
    
    if(K == 0 or K == 1):
        return 1
    
    counter[0] = 1

    print(counter)
    #Iterate over all values from 1-k
    for i in range(1, K + 1):
        #calculate all of the possible combinations within the current sub-value. 
        for j in range(i):
            #counter[j] represents the left side of the subtree, counter[i - j - 1] represents the right side of the subtree
            
            counter[i] += counter[j] * counter[i - j - 1]
    
    return counter[K]

print(binaryTreeCounter(5))

