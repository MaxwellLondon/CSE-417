import random

class intervalSchedule:
    def __init__(self, intervalSet = {}):
       self.intervals = intervalSet

    def randomIntervalGenerator(self, N, startPosition, maxLength, maxValue):
        intervals = {i: {} for i in range(0, N)}

        for i in range(len(intervals)):
            startRange = range(1, startPosition + 1)
            lengthRange = range(1, maxLength + 1)
            valueRange = range(1, maxValue + 1)

            startValue = random.choice(startRange)
            lengthValue = random.choice(lengthRange)
            value = random.choice(valueRange)

            intervals[i] = {"start": startValue, "length": lengthValue, "value": value}

        self.intervals = intervals

        return self.intervals

    def earliestStartTime(self):
        # Sort intervals by start time
        sorted_intervals = sorted(self.intervals.values(), key=lambda x: x["start"])

        # Initialize variables
        schedule = []
        last_finish = 0

        # Loop through intervals
        for interval in sorted_intervals:
            # Check if interval overlaps with previous interval
            if interval["start"] >= last_finish:
                schedule.append(interval)
                last_finish = interval["start"] + interval["length"]

        return sum(map(lambda x: x['value'], schedule))
    
    def maximumValueFirst(self):
        # Sort intervals by value in descending order
        sorted_intervals = sorted(self.intervals.values(), key=lambda x: x["value"], reverse=True)

        # Initialize variables
        schedule = []
        last_finish = 0

        # Loop through intervals
        for interval in sorted_intervals:
            # Check if interval overlaps with previous interval
            if interval["start"] >= last_finish:
                schedule.append(interval)
                last_finish = interval["start"] + interval["length"]

        return sum(map(lambda x: x['value'], schedule))
    
    def maximumValueDensityFirst(self):
        # Sort intervals by value in descending order
        sorted_intervals = sorted(self.intervals.values(), key=lambda x: x["value"] / x["length"], reverse=True)

        # Initialize variables
        schedule = []
        last_finish = 0

        # Loop through intervals
        for interval in sorted_intervals:
            # Check if interval overlaps with previous interval
            if interval["start"] >= last_finish:
                schedule.append(interval)
                last_finish = interval["start"] + interval["length"]

        return sum(map(lambda x: x['value'], schedule))
    
    def dynamicProgrammingSolution(self):
        if len(self.intervals) == 0:
            return 0
        
        sorted_intervals = sorted(self.intervals.values(), key=lambda x: x["start"])
        
        maxValue = [0] * len(sorted_intervals)

        for i in range(len(sorted_intervals)):
            for j in range(i):
                #If any of the previous intervals end before the current interval starts and the max value used to get to that interval is greater than the value of the current interval.
                
                if sorted_intervals[j]["start"] + sorted_intervals[j]["length"] <= sorted_intervals[i]["start"] and maxValue[j] > maxValue[i]:
                    #We now know that the previous intervals are compatible with the current one, therefore we can imply we can attain the same value accesed there while including the crrent interval. 
                    maxValue[i] = maxValue[j]
            
            #We now add the value of the current interval on top of the maximum value of any previosuly attained intervals that are compatible. 
            maxValue[i] += sorted_intervals[i]["value"]

        return max(maxValue)
    

i = intervalSchedule()

#i.randomIntervalGenerator(N = 10000, startPosition = 1000000, maxLength = 2000, maxValue = 100)

#print(i.earliestStartTime())
# print(i.maximumValueFirst())
# print(i.maximumValueDensityFirst())
# print(i.dynamicProgrammingSolution())



for n in range(0, 10):
    i.randomIntervalGenerator(N = 10000, startPosition = 1000000, maxLength = 2000, maxValue = 100)
    print((i.earliestStartTime(), i.maximumValueFirst(), i.maximumValueDensityFirst(), i.dynamicProgrammingSolution()))
 


# (45483, 299, 747, 111989)
# (44627, 1371, 938, 111300)
# (47272, 387, 666, 111728)
# (47698, 875, 307, 111071)
# (44818, 787, 468, 109800)
# (44769, 694, 684, 112439)
# (45107, 595, 596, 108836)
# (45484, 600, 676, 112258)
# (47611, 685, 640, 113787)
# (45513, 790, 407, 113268)