import random

def permutation(n):
    # Create a list of numbers from 0 to n-1
    nums = list(range(n))
    # Iterate through the list
    for i in range(n):
        # Generate a random index between i and n-1
        rand_index = random.randint(i, n-1)
        # Swap the current number with the randomly generated index
        nums[i], nums[rand_index] = nums[rand_index], nums[i]
    return nums

def generatePermutations(N):
    mPreferences = []
    wPreferences = []

    for i in range (0, N):
        mPreferences.append(permutation(N))
        wPreferences.append(permutation(N))

    return (mPreferences, wPreferences)

def stableMatching(n, mPreferences = [], wPreferences = []):
    unmatchedMs = list(range(n))

    mPartner = [-1 for i in range(n)]
    wPartner = [-1 for i in range(n)]

    #This keeps track of the count of proposals for each M. The corrosponding index will be incremented whenever an M proposes. 
    # The index is associated with the current count of proposals performed by M.
    nextMProposal = [0] * n   

    while len(unmatchedMs) != 0:
        #Grab the first unmatched M
        currentM = unmatchedMs[0]
        #Grab the current Ms preference list from the preference array. 
        currentMPreferences = mPreferences[currentM]
        #Grab the index of the next proposal for the based on the index held in the nextMProposal array 
        currentW = currentMPreferences[nextMProposal[currentM]]
        #Grab the preferences of the W who will be proposed to.
        currentWPreferences = wPreferences[currentW]
        #Grab the current match for the W
        currentWMatch = wPartner[currentW]


        #Time to handle the first case, when the current W does not have a match (-1 indicates there is no match)

        if(currentWMatch == -1):
            #Assign the M and W together. 
            mPartner[currentM] = currentW
            wPartner[currentW] = currentM

            #Update the current proposal order for the current M
            nextMProposal[currentM] += 1
            #Remove the current M from the unmatchedMs array.
            unmatchedMs.pop(0)

        else:
            #Time to handle the second case when a pairing with the current W already exists 
            #Now we must grab the index of the preference for the currently matched M and the proposing M on the proposed W. We will then compare the priority.


            #preference index of the current match
            matchedMPreferenceIndex = currentWPreferences.index(currentWMatch)

            #preference index of the proposing M
            currentMPreferenceIndex = currentWPreferences.index(currentM)

            if(currentMPreferenceIndex > matchedMPreferenceIndex):
                #Create the new matching
                wPartner[currentW] = currentM
                mPartner[currentM] = currentW
                #Update the next proposal for the current M
                nextMProposal[currentM] += 1

                #Remove the current M because they were matched
                unmatchedMs.pop(0)
                #Add the previously matched M to be matched again
                unmatchedMs.insert(0, currentWMatch)

            else:
                #If the proposal fails, then move on to the next W
                nextMProposal[currentM] += 1
    mSum = 0     
    wSum = 0 
    for i in range(0, n):
        currentPlacementInMPreference = mPreferences[i].index(mPartner[i])

        currentPlacementInWPreference = wPreferences[i].index(wPartner[i])

        # print(str(i) + " M placement in preference order")
        # print(currentPlacementInMPreference)
        # print(str(i) + " W placement in preference order")
        # print(currentPlacementInWPreference)

        mSum += currentPlacementInMPreference

        wSum += currentPlacementInWPreference

    print("weight")
    print((mSum / n, wSum / n))

    return (mPartner, wPartner)


#Test case

for i in range (0, 1000):
    result = generatePermutations(i)
    #print(i)

    print("M Permutation")
    print(result[0]) 
    print("W Permutation")
    print(result[1])
    print(stableMatching(i, result[0], result[1]))

    


# print("M Permutation")
# print(result[0]) 
# print("W Permutation")
# print(result[1])








