# Solution to the Active Select problem using a Greedy Algorithm

#Description:
# 1. Take a list containing the start time and finish time of a "job" (assume sorted based on finish times)
start = [10,12,20]
stop =  [20,25,30]

# 2. Take the job that finishes the soonest relative to the current time
accepted = 0
i = 0
while i < len(stop): # stop chosen arbitrarily as end, start would work too
    if start[i] >= accepted: # if the current start value is of equal or greater value than the last accepted job's end...
        print(i) 
        accepted = stop[i] # store the current job's end in accepted
    i = i + 1

# This algorithm is greedy because it looks at the first (closest) end time and starts the algorithm from there. 
# From that spot it continues taking the next available job.