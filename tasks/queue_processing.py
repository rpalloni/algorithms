# calculate minimum time to process a set of tasks by a queue given:
# the maximum number of tasks in a batch
# the time to process a single batch
# the number of tasks the queue must process

def minTime(batchSize, processingTime, numTasks):
    output = []
    queues = 2
    for i in range(queues):
        q_batchSize = batchSize[i]
        q_processingTime = processingTime[i]
        q_numTasks = numTasks[i]

        nbatch, rem = divmod(q_numTasks, q_batchSize)
        if rem != 0:
            nbatch += 1 # add a batch for remaining tasks
        time = nbatch * q_processingTime
        output.append(time)

    return output

# queue 0 can process a maximum of 4 tasks in 6 minutes
# queue 1 can process a maximum of 3 tasks in 5 minutes 
# each queue has 8 tasks
batchSize = [4, 3]
processingTime = [6, 5]
numTasks = [8, 8]

minTime(batchSize, processingTime, numTasks) # result 12, 15
