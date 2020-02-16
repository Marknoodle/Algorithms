# Solution to the Active Select problem using a Greedy Algorithm

# Description:
# 1. Take a list containing the start time and finish time of a "job" (assume sorted based on finish times)
startTime = [1,3,0,5,8,5]
stopTime =  [2,4,6,7,9,9]

# 2. Take the job that finishes the soonest relative to the current time
def act_sel(startList, finishList):
    accepted = 0
    i = 0
    while i < len(finishList): # stop chosen arbitrarily as end, start would work too
        if startList[i] >= accepted: # if the current start value is of equal or greater value than the last accepted job's end...
            print(i) 
            accepted = finishList[i] # store the current job's end in accepted
        i = i + 1

# This algorithm is greedy because it looks at the first (closest) end time and starts the algorithm from there. 
# From that spot it continues taking the next available job.

# Now, what if we are given two unsorted lists?
# Let's sort them ourselves!

# Description:
# 1. take each list, and associate them in tuples of (start,finish), and then sort them based on stop time (zip them then sort them)
def stopSorter(start, stop):
    zipped = list(zip(start,stop))
    zipped.sort(key=secondValReturner)
    start, stop = zip(*zipped)
    return list(start),list(stop)

def secondValReturner(val):
    return val[1]

first,second = stopSorter(startTime,stopTime)
act_sel(first,second)
     

