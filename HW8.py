def subset_sum_count(S, K):
    N = len(S)

    matrix = [[0] * (K+1) for _ in range(N + 1)]

    matrix[0][0] = 1

    for i in range(1, N + 1):
        matrix[i][0] = 1
        for j in range(1, K + 1):
            matrix[i][j] = matrix[i-1][j]
            if j >= S[i-1]:
                matrix[i][j] += matrix[i-1][j-S[i-1]]
    
    for i in range(0, len(matrix)):
        print(matrix[i])

def smallest_subset_sum(S, K):
    n = len(S)
    matrix = [ [ 0 if j == 0 else float('inf') for j in range(K+1)] for i in range(n+1) ]
    
    for i in range(1, n+1):
        for j in range(1, K+1):
            #Number is not included in the subset sum. bring down value from one row up in matrix. 
            if j < S[i-1]:
                matrix[i][j] = matrix[i-1][j]
            #Number is included in the subset sum, compute the minimum from one row up in matrix compared to one row up in the matrix - S[i]
            # which finds the complementary value for the given number in S. If the value is not carried over, then we add 1 to indicate that another number has been selected.
            else:
                matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-S[i-1]]+1)
    
    if matrix[n][K] == float('inf'):
        return "subset sum not found"
    else:
        for i in range(0, len(matrix)):
            return matrix[n][K]


# # Test Case 1
# S = [2, 3, 5, 7]
# K = 10
# print(smallest_subset_sum(S, K))

# # Test Case 2
# S = [1, 2, 3, 4]
# K = 8
# print(smallest_subset_sum(S, K))

# # Test Case 3
# S = [5, 6, 7]
# K = 2
# print(smallest_subset_sum(S, K))

# # # Test Case 4
# S = [5, 6, 7]
# K = 7
# print(smallest_subset_sum(S, K))

# # # Test Case 5
# S = [1, 3, 4, 9, 10]
# K = 2
# print(smallest_subset_sum(S, K))

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida",
"Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts",
"Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico",
"New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina",
"South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

electoralVotes1964 = [10,3,5,6,40,6,8,3,3,14,12,4,4,26,13,9,7,9,10,4,10,14,21,10,7,12,4,5,3,4,17,4,43,13,4,26,8,6,29,4,8,4,11,25,4,3,12,9,7,12,3]

electoralVotes1972 = [9,3,6,6,45,7,8,3,3,17,12,4,4,26,13,8,7,9,10,4,10,14,21,10,7,12,4,5,3,4,17,4,41,13,3,25,8,6,27,4,8,4,10,26,4,3,12,9,6,11,3]

electoralVotes1984 = [9,3,7,6,47,8,8,3,3,21,12,4,4,24,12,8,7,9,10,4,10,13,20,10,7,11,4,5,4,4,16,5,36,13,3,23,8,7,25,4,8,3,11,29,5,3,12,10,6,11,3]

electoralVotes1992 = [9,3,8,6,54,8,8,3,3,25,13,4,4,22,12,7,6,8,9,4,10,12,18,10,7,11,3,5,4,4,15,5,33,14,3,21,8,7,23,4,8,3,11,32,5,3,13,11,5,11,3]

electoralVotes2004 = [9,3,10,6,55,9,7,3,3,27,15,4,4,21,11,7,6,8,9,4,10,12,17,10,6,11,3,5,5,4,15,5,31,15,3,20,7,7,21,4,8,3,11,34,5,3,13,11,5,10,3]

electoralVotes2012 = [9,3,11,6,55,9,7,3,3,29,16,4,4,20,11,6,6,8,8,4,10,11,16,10,6,10,3,5,6,4,14,5,29,15,3,18,7,7,20,4,9,3,11,38,6,3,13,12,5,10,3]

electoralVotes2024 = [9,3,11,6,54,10,7,3,3,30,16,4,4,19,11,6,6,8,8,4,10,11,15,10,6,10,4,5,6,4,14,5,28,16,3,17,7,8,19,4,9,3,11,40,6,3,13,12,4,10,3]

test = [1, 2, 3, 4]

def countPartitions(electoralVotes):
    N = len(electoralVotes)

    halfSum = sum(electoralVotes) // 2
    
    #Create matrix of 270 X 51
    matrix = [[0 for j in range(halfSum + 1)] for i in range(N + 1)]

    #Initial case for empty subsets, only one possible outcome. 
    for i in range(N + 1):
        matrix[i][0] = 1

    #Driving loop to iterate and access all subproblems. 
    for i in range(1, N+1):
        for j in range(1, halfSum + 1):
            #If the current number is greater than the current subset sum, then it cannot be considered. 
            if electoralVotes[i - 1] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i - 1][j] + matrix[i - 1][j - electoralVotes[i - 1]]

    return matrix[N][halfSum]
            

        
def minCountPartition(electoralVotes):
    N = len(electoralVotes)

    halfSum = sum(electoralVotes) // 2
    
    #Create matrix of 270 X 51
    matrix = [[0 for j in range(halfSum + 1)] for i in range(N + 1)]

    #Initial case for empty subsets, only one possible outcome. 
    for i in range(N + 1):
        matrix[i][0] = 1

    #Driving loop to iterate and access all subproblems. 
    for i in range(1, N+1):
        for j in range(1, halfSum + 1):
            #If the current number is greater than the current subset sum, then it cannot be considered. 
            if electoralVotes[i - 1] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i - 1][j] + matrix[i - 1][j - electoralVotes[i - 1]]

    min_elements = []
    i, j = N, halfSum
    while j > 0:
        if matrix[i-1][j]:
            i -= 1
        elif matrix[i-1][j-electoralVotes[i-1]]:
            min_elements.append(electoralVotes[i-1])
            j -= electoralVotes[i-1]
            i -= 1

    return len(min_elements), sorted(min_elements)


print(minCountPartition(electoralVotes2024)[1])


def get_states_with_votes(votes, electoral_votes, states):
    states_with_votes = {}
    for i, vote in enumerate(electoral_votes):
        if vote not in states_with_votes:
            states_with_votes[vote] = []
        states_with_votes[vote].append(states[i])
    result = []
    for vote in votes:
        if vote in states_with_votes and states_with_votes[vote]:
            result.append(states_with_votes[vote].pop())
    return result



print(get_states_with_votes(minCountPartition(electoralVotes2024)[1], electoralVotes2024, states))