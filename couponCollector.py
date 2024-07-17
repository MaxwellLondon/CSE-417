import random as r

def permutation(n):
    # Create a list of numbers from 0 to n-1
    nums = list(range(n))
    # Iterate through the list
    for i in range(n):
        # Generate a random index between i and n-1
        rand_index = r.randint(i, n-1)
        # Swap the current number with the randomly generated index
        nums[i], nums[rand_index] = nums[rand_index], nums[i]
    return nums


def couponCollector(n):
    coupons = permutation(n)
    couponSet = set()
    iterations = 0
    while(len(couponSet) < n):
        #Generate random coupon
        coupon = coupons[r.randint(0, n - 1)]
        couponSet.add(coupon)
        iterations += 1
    
    print("Coupons Collected: " + str(iterations), "N: " + str(n) + ", Ratio of collected coupons to n " + str(iterations / n))

def couponCollector2(n):
    coupons = permutation(n)
    couponDict = {n: -1 for n in range(0, n)}

    couponCount = 0
    iterations = 0

    while(couponCount < n):
        couponIndex = coupons[r.randint(0, n-1)]
        couponValue = r.randint(0, n-1)
        iterations += 1

        if(couponDict[couponIndex] > couponValue or couponDict[couponIndex] == -1):
            if(couponDict[couponIndex] == -1):
                couponCount += 1
            couponDict[couponIndex] = couponValue

    couponValueSum = 0
    for key in couponDict.keys():
        couponValueSum += couponDict[key]
        
    
    return ("COUPON VALUE SUM: " + str(couponValueSum), "COUPON VALUE SUM / N: " + str(couponValueSum/n))
    

    



#Test Case
# for i in range(200, 4001, 200):
#     couponCollector(i)


for i in range(200, 4001, 200):
    print(couponCollector2(i))



